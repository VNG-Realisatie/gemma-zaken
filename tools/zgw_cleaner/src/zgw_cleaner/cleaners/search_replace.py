
from typing import Dict, Any, List
from ..cleaner import Cleaner
from copy import deepcopy

class SearchReplaceCleaner(Cleaner):
    """Search and replace exact dictionary keys and values in the OpenAPI spec."""

    def __init__(self):
        super().__init__('search-replace')

        # TODO make this file-based
        self.patterns = [
            { 'search': { '204': { 'description': 'No content' }},
              'replace': { '204': { 'description': 'No content',
                                   'headers': { 'API-version': { 'schema': 'string',
                                                                 'description': 'Geeft een specifieke API-versie aan in de context van een specifieke aanroep. Voorbeeld: 1.2.1.' } } } }
            },
        ]

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by searching and replacing exact dictionary keys and values"""
        if path is None:
            path = []
            
        if not isinstance(spec, dict):
            return spec
        
        for pattern in self.patterns:
            pattern_matched = True
            for search_key, search_values in pattern['search'].items():
                if search_key not in spec:
                    pattern_matched = False
                    break
                # check internal integrety of pattern
                if search_key not in pattern['replace']:
                    pattern_matched = False
                    break
                
                if spec[search_key] != search_values:
                    pattern_matched = False
                    break
            if not pattern_matched:
                continue

            for search_key in pattern['search'].keys():
                spec[search_key] = deepcopy(pattern['replace'][search_key])

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key])
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key]) if isinstance(item, dict) else item 
                            for item in value]

        return spec
