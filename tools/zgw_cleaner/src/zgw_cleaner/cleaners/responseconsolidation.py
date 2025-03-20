from typing import Dict, Any, List
import logging
from copy import deepcopy
from ..cleaner import Cleaner
from ruamel.yaml.scalarstring import SingleQuotedScalarString

class ResponseConsolidationCleaner(Cleaner):
    """
    Consolidates response patterns at the operation level following OpenAPI's matching rules.
    Consolidates from specific to unspecific (exact code -> 4xx/5xx).
    """
    def _revert_consolidation_by_number(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Reverts the consolidation of responses by number."""

        if 'components' not in spec:
            return spec
        if 'responses' not in spec['components']:
            return spec
        if 'paths' not in spec:
            return spec
        
        response_codes = ['default', '1XX', '2XX', '3XX', '4XX', '5XX', '400', '401', '403',
                          '404', '405', '406', '409', '410', '412', '415', '429', '500', '501',
                          '502', '503', '504']
        
        responses = spec['components']['responses']
        response_map = {}
        for response_key, response_def in responses.items():
            if str(response_key) in response_codes:
                response_map[response_key] = response_def

        for path, path_item in spec['paths'].items():
            for method, operation in path_item.items():
                if 'responses' not in operation:
                    continue

                for response_key, response_def in operation['responses'].items():
                    if str(response_key) in response_map:
                        operation['responses'][response_key] = response_map[response_key]

        for response_code in response_codes:
            if response_code in responses:
                responses.pop(response_code)

        return spec

    def _create_response_key(self, response_def: Dict) -> frozenset:
        """Creates a hashable key from a response definition, ignoring description."""
        if not isinstance(response_def, dict):
            return frozenset()

        key_items = []
        for k, v in response_def.items():
            if k == 'description':
                continue
            if isinstance(v, dict):
                v = tuple(sorted((sk, str(sv)) for sk, sv in v.items()))
            key_items.append((k, str(v)))
        return frozenset(key_items)

    def _consolidate_operation_responses(self, responses: Dict) -> Dict:
        """Consolidate responses within a single operation."""
        if not responses:
            return responses

        # Skip if already contains pattern responses
        if any(code in ['4xx', '5xx', 'default'] for code in responses):
            return responses

        # Group responses by pattern
        patterns = {}
        for status_code, response in responses.items():
            key = self._create_response_key(response)
            if key not in patterns:
                patterns[key] = {
                    'pattern': {k: v for k, v in response.items() if k != 'description'},
                    'codes': set()
                }
            patterns[key]['codes'].add(status_code)

        # Find patterns to consolidate
        for pattern_info in patterns.values():
            codes = pattern_info['codes']
            pattern = pattern_info['pattern']
            
            # Skip if only one occurrence
            if len(codes) <= 1:
                continue

            # Group status codes
            client_errors = {code for code in codes if code.startswith('4')}
            server_errors = {code for code in codes if code.startswith('5')}

            # Consolidate based on patterns found
            to_remove = set()
            if len(client_errors) > 1:
                pattern_copy = {'description': 'Client error'}
                pattern_copy.update(pattern)
                responses[SingleQuotedScalarString('4XX')] = pattern_copy
                to_remove.update(client_errors)
                self.stats.counts['4xx_patterns_created'] = self.stats.counts.get('4xx_patterns_created', 0) + 1

            if len(server_errors) > 1:
                pattern_copy = {'description': 'Server error'}
                pattern_copy.update(pattern)
                responses[SingleQuotedScalarString('5XX')] = pattern_copy
                to_remove.update(server_errors)
                self.stats.counts['5xx_patterns_created'] = self.stats.counts.get('5xx_patterns_created', 0) + 1

            # Remove consolidated responses
            for code in to_remove:
                responses.pop(code, None)
                self.stats.counts['responses_consolidated'] = self.stats.counts.get('responses_consolidated', 0) + 1

        return responses

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by consolidating common response patterns."""
        if path is None:
            path = []
            spec = self._revert_consolidation_by_number(spec)

        if not isinstance(spec, dict):
            return spec

        if 'responses' in spec and path != ['components']:
            spec['responses'] = self._consolidate_operation_responses(spec['responses'])

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                spec[key] = self.clean(value, path + [key])

        return spec
