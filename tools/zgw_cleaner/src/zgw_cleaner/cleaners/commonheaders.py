from typing import Dict, Any
import logging
from ..core import Cleaner
from copy import deepcopy

class CommonHeadersCleaner(Cleaner):
    """Moves common header definitions to components/headers."""
    
    def __init__(self):
        super().__init__()
        self.common_headers = {}

    def _ref_name(self, header_name: str) -> str:
        """Generate reference name for a header."""
        # Remove special characters, could add more replacements as needed
        return header_name.replace('-', '')        

    def _extract_header_def(self, headers: Dict) -> None:
        """Extract header definitions and count occurrences."""
        for header_name, header_def in headers.items():
            # Skip if it's already a reference
            if '$ref' in header_def:
                continue
            
            # Create a hashable key from the header definition
            try:
                header_items = []
                for k, v in header_def.items():
                    if isinstance(v, dict):
                        v = tuple(sorted((sk, str(sv)) for sk, sv in v.items()))
                    header_items.append((k, str(v)))
                header_key = frozenset(header_items)
            except TypeError as e:
                logging.warning(f"Could not create key for header {header_name}: {e}")
                continue

            if header_key not in self.common_headers:
                self.common_headers[header_key] = {
                    'name': header_name,
                    'definition': header_def,
                    'count': 1
                }
            else:
                self.common_headers[header_key]['count'] += 1

    def _collect_headers(self, spec: Dict[str, Any]) -> None:
        """First pass: collect all header definitions."""
        if isinstance(spec, dict):
            # Skip only components/headers during collection
            if 'components' in spec and 'headers' in spec['components']:
                # Process other components sections, just skip 'headers'
                for key, value in spec['components'].items():
                    if key != 'headers':
                        self._collect_headers(value)
                return
                
            if 'headers' in spec:
                self._extract_header_def(spec['headers'])
            
            # Recurse through nested structures
            for key, value in spec.items():
                self._collect_headers(value)
        
        elif isinstance(spec, list):
            for item in spec:
                self._collect_headers(item)

    def _add_common_headers_to_components(self, spec: Dict[str, Any]) -> Dict[str, Any]:

        # Initialize components/headers if needed
        if 'components' not in spec:
            spec['components'] = {}
        if 'headers' not in spec['components']:
            spec['components']['headers'] = {}

        # Add common headers to components/headers    
        for header_info in self.common_headers.values():
            ref_name = self._ref_name(header_info['name'])
            spec['components']['headers'][ref_name] = deepcopy(header_info['definition'])
            self.stats.counts['headers_collected'] += 1

        return spec

    def _replace_common_headers_with_refs(self, spec: Dict[str, Any], path: list = []) -> Dict[str, Any]:
        """Replace header definitions with refs."""

        if isinstance(spec, list):
            return [self._replace_common_headers_with_refs(item, path) for item in spec]

        if not isinstance(spec, dict):
            return spec

        # Skip if we're in components/headers

        if not path == ['components'] and 'headers' in spec:
            headers = spec['headers']

            for header_name, header_def in list(headers.items()):
                if '$ref' in header_def:
                    continue
            
                # Create the same key as used in collection
                header_items = []
                for k, v in header_def.items():
                    if isinstance(v, dict):
                        v = tuple(sorted((sk, str(sv)) for sk, sv in v.items()))
                    header_items.append((k, str(v)))
                header_key = frozenset(header_items)

                # If the header is common, replace it with a ref
                header_info = self.common_headers.get(header_key)
                if header_info:
                    ref_name = self._ref_name(header_info['name'])
                    headers[header_name] = {'$ref': f'#/components/headers/{ref_name}'}
                    self.stats.counts['headers_replaced'] += 1

        # Recurse through nested structures with path tracking
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                new_path = path + [key]
                spec[key] = self._replace_common_headers_with_refs(value, new_path)

        return spec


    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Clean the specification by consolidating common headers."""
        if not isinstance(spec, dict):
            return spec

        # First pass: collect headers
        self._collect_headers(spec)

        self.stats.counts['unique_headers'] = len([h for h in self.common_headers.values() if h['count'] == 1])

        # Only process headers that appear multiple times
        self.common_headers = {k: v for k, v in self.common_headers.items() if v['count'] > 1}
        if self.common_headers:
            self.stats.counts['common_headers'] = len([h for h in self.common_headers.values() if h['count'] > 1])

            # Second pass: move common headers to components
            spec = self._add_common_headers_to_components(spec)

            # Third pass: replace headers with refs
            spec = self._replace_common_headers_with_refs(spec)

        return spec
