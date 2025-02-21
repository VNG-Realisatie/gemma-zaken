from typing import Dict, Any
import logging
from copy import deepcopy
from ..core import Cleaner

class OperationResponsesCleaner(Cleaner):
    """
    Consolidates response patterns at the operation level following OpenAPI's matching rules.
    Consolidates from specific to unspecific (exact code -> 4xx/5xx -> default).
    """

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
                responses['4xx'] = pattern_copy
                to_remove.update(client_errors)
                self.stats.counts['4xx_patterns_created'] = self.stats.counts.get('4xx_patterns_created', 0) + 1

            if len(server_errors) > 1:
                pattern_copy = {'description': 'Server error'}
                pattern_copy.update(pattern)
                responses['5xx'] = pattern_copy
                to_remove.update(server_errors)
                self.stats.counts['5xx_patterns_created'] = self.stats.counts.get('5xx_patterns_created', 0) + 1

            if client_errors and server_errors:
                pattern_copy = {'description': 'Generic error'}
                pattern_copy.update(pattern)
                responses['default'] = pattern_copy
                responses.pop('4xx', None)
                responses.pop('5xx', None)
                to_remove.update(client_errors | server_errors)
                self.stats.counts['default_patterns_created'] = self.stats.counts.get('default_patterns_created', 0) + 1

            # Remove consolidated responses
            for code in to_remove:
                responses.pop(code, None)
                self.stats.counts['responses_consolidated'] = self.stats.counts.get('responses_consolidated', 0) + 1

        return responses

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Clean the specification by consolidating common response patterns."""
        if not isinstance(spec, dict):
            return spec

        if 'responses' in spec:
            spec['responses'] = self._consolidate_operation_responses(spec['responses'])

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                spec[key] = self.clean(value)

        return spec
