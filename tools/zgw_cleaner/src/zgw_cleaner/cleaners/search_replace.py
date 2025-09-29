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
                                   'headers': { 'API-version': { 'schema': { 'type': 'string' },
                                                                 'description': 'Geeft een specifieke API-versie aan in de context van een specifieke aanroep. Voorbeeld: 1.2.1.' } } } }
            },
        ]
    
        self.patterns_by_path = [
            { 'search': ['servers'],
              'replace': { 'servers': [ {'url': 'https://{host}/{basePath}/v1',
                                         'variables': {
                                             'host': { 'default': 'example.com',
                                                      'description': 'De hostserver voor de API' },
                                            'basePath': { 'default': 'api',
                                                          'description': 'Het basispad voor de API' }
                                         }} ] } 
            },
            { 'search': ['info', 'license'],
              'replace': { 'license': { 'name': 'European Union Public Licence (EUPL-1.2)',
                                        'url': 'https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12' } }
            },
            { 'search': ['openapi'],
             'replace': { 'openapi': '3.0.4' } },
            { 'search': ['info', 'contact'],
              'replace': { 'contact': { 'url': 'https://github.com/VNG-Realisatie/gemma-zaken',
                                       'email': 'standaarden.ondersteuning@vng.nl' } } },
        ]

        # Rules to rewrite $ref URLs to local relative files. Easy to extend later.
        # Each rule matches on the base (before any #fragment) containing the given substring.
        # The fragment, if present, is preserved.
        self.ref_url_rewrites: List[Dict[str, str]] = [
            {
                'contains': 'ztc/current_version/openapi.yaml',
                'replace_with': '../catalogi/openapi.yaml',
            },
            {
                'contains': 'drc/current_version/openapi.yaml',
                'replace_with': '../documenten/openapi.yaml',
            },
            {
                'contains': 'zrc/current_version/openapi.yaml',
                'replace_with': '../zaken/openapi.yaml',
            },
            {
                'contains': 'brc/current_version/openapi.yaml',
                'replace_with': '../besluiten/openapi.yaml',
            },
        ]

    def _rewrite_ref(self, ref_value: str) -> str:
        """Rewrite $ref values based on configured rules, preserving #fragments."""
        if not isinstance(ref_value, str):
            return ref_value

        # Split off fragment if present
        if '#' in ref_value:
            base, fragment = ref_value.split('#', 1)
            fragment = '#' + fragment
        else:
            base, fragment = ref_value, ''

        for rule in getattr(self, 'ref_url_rewrites', []) or []:
            contains = rule.get('contains')
            replacement = rule.get('replace_with')
            if contains and replacement and contains in base:
                return f"{replacement}{fragment}"

        return ref_value

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

        for pattern in self.patterns_by_path:
            if pattern['search'][-1] not in spec:
                continue
            if pattern['search'][:-1] != path:
                continue
            spec[pattern['search'][-1]] = deepcopy(pattern['replace'][pattern['search'][-1]])

        # Rewrite $ref values according to ref_url_rewrites
        for k, v in list(spec.items()):
            if k == '$ref' and isinstance(v, str):
                new_ref = self._rewrite_ref(v)
                if new_ref != v:
                    spec[k] = new_ref

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key])
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key]) if isinstance(item, dict) else item 
                            for item in value]

        return spec
