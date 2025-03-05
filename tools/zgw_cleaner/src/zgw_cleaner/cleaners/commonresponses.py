from typing import Dict, Any
import logging
from ..core import Cleaner
from copy import deepcopy
from caseconverter import pascalcase

class CommonResponsesCleaner(Cleaner):
    """
    Creates reusable response patterns in components/responses.
    
    This cleaner identifies common response patterns used across multiple
    endpoints and moves their definitions to the components/responses section
    of the OpenAPI specification.
    """
    
    def __init__(self):
        super().__init__()
        self.error_patterns = {}
        
    def _extract_error_pattern(self, response_def: Dict) -> frozenset:
        """Extract the core pattern from an error response."""
        if not isinstance(response_def, dict):
            return frozenset()
            
        pattern_items = []
        if 'content' in response_def:
            content = response_def['content']
            if 'application/problem+json' in content:
                problem = content['application/problem+json']
                if 'schema' in problem:
                    # Store the schema reference or structure
                    pattern_items.append(('schema', str(problem['schema'])))
                    
        if 'headers' in response_def:
            headers = response_def['headers']
            for header_name, header_def in sorted(headers.items()):
                pattern_items.append(('header', f"{header_name}:{str(header_def)}"))
                
        return frozenset(pattern_items)

    def _generate_pattern_name(self, response: Dict, status_code: str) -> str:
        """Generate a meaningful name for the response pattern."""
        try:
            schema = response.get('content', {}).get('application/problem+json', {}).get('schema', {})
        
            if isinstance(schema, dict) and '$ref' in schema:
                # Extract name from schema reference
                schema_name = schema['$ref'].split('/')[-1]
                return f"{schema_name}Response"
        
            # Fallback to status code based name
            return f"Status{status_code}Response"
        
        except Exception as e:
            logging.warning(f"Could not generate pattern name: {e}")
            return f"Status{status_code}Response"

    def _generate_description(self, schema_ref: str) -> str:
        """Generate a meaningful description from the schema reference."""
        schema_name = schema_ref.split('/')[-1]

       # Add more logic to generate a meaningful description if needed
       # For now, just return the schema name in a readable format
       # Example: "Fout - fout"
        return f"{schema_name} - {schema_name.lower()}"

    def _collect_and_create_patterns(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Collect error patterns and create reusable components."""
        paths = spec.get('paths', {})
    
        # First pass: collect patterns
        for path in paths.values():
            for operation in path.values():
                if isinstance(operation, dict) and 'responses' in operation:
                    responses = operation['responses']
                    for status_code, response in responses.items():
                        # Focus on error responses (4xx, 5xx)
                        if not str(status_code).startswith(('4', '5')):
                            continue
                        
                        pattern = self._extract_error_pattern(response)
                        if pattern:
                            if pattern not in self.error_patterns:
                                name = self._generate_pattern_name(response, status_code)
                                self.error_patterns[pattern] = {
                                    'name': name,
                                    'definition': deepcopy(response),
                                    'count': 1
                                }
                            else:
                                self.error_patterns[pattern]['count'] += 1

        # Create components for frequently used patterns
        if 'components' not in spec:
            spec['components'] = {}
        if 'responses' not in spec['components']:
            spec['components']['responses'] = {}
    
        for pattern_info in self.error_patterns.values():
            if pattern_info['count'] > 1:
                name = pattern_info['name']
                definition = pattern_info['definition']
            
                # Update description based on the schema reference
                schema_ref = definition.get('content', {}).get('application/problem+json', {}).get('schema', {}).get('$ref', '')
                if schema_ref:
                    definition['description'] = self._generate_description(schema_ref)
            
                spec['components']['responses'][name] = definition
                self.stats.counts['response_patterns_created'] = \
                    self.stats.counts.get('response_patterns_created', 0) + 1
                
        return spec

    def _replace_with_refs(self, spec: Dict[str, Any], path: list = []) -> Dict[str, Any]:
        """Replace response definitions with refs to common patterns."""
        if isinstance(spec, list):
            return [self._replace_with_refs(item, path) for item in spec]

        if not isinstance(spec, dict):
            return spec

        # Process responses sections, but skip components/responses
        if not path == ['components'] and 'responses' in spec:
            responses = spec['responses']
        
            for status_code, response_def in list(responses.items()):
                # Skip if already a reference
                if '$ref' in response_def:
                    continue
                
                # Skip non-error responses
                if not str(status_code).startswith(('4', '5')):
                    continue

                # Create pattern key
                pattern = self._extract_error_pattern(response_def)
            
                # If the pattern matches a common one, replace with ref
                if pattern in self.error_patterns:
                    pattern_info = self.error_patterns[pattern]
                    if pattern_info['count'] > 1:
                        responses[status_code] = {
                            '$ref': f'#/components/responses/{pattern_info["name"]}'
                        }
                        self.stats.counts['responses_replaced'] = \
                            self.stats.counts.get('responses_replaced', 0) + 1

        # Recurse through nested structures with path tracking
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                new_path = path + [key]
                spec[key] = self._replace_with_refs(value, new_path)

        return spec

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Create reusable response patterns and update references."""
        if not isinstance(spec, dict):
            return spec
            
        spec = self._collect_and_create_patterns(spec)

        # Replace matching patterns with references
        if self.error_patterns:
            spec = self._replace_with_refs(spec)
            
        return spec
