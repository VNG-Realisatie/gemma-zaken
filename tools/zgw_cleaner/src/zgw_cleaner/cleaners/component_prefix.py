from typing import Dict, Any, List
from ..cleaner import Cleaner

class ComponentPrefixCleaner(Cleaner):
    """
    Restructures component schemas by removing prefix variants and merging with base schemas.
    """
    def __init__(self):
        super().__init__('merge-prefix-components')
        self.search_replace = []

    def _find_concrete_type(self, name: str, spec: Dict[str, Any]) -> bool:
        """
        Checks if the schema is a prefix variant that just references the prefixed schema.
        Example: 'zrc' referencing 'zrcAutorisatie'
        """

        if not isinstance(spec, dict) or 'allOf' not in spec:
            return None

        # Should be only allOf
        if not self._is_mixin_schema(spec):
            return None
        
        # Collect the refs
        refs = []
        for ref in spec['allOf']:
            refs.append(ref['$ref'])

        # Check if one ref points to a schema with name's prefix
        prefix = name.lower()
        for ref in refs:
            short_ref = ref.replace('#/components/schemas/', '')
            if short_ref.startswith(prefix):
                return short_ref

        return None

    def _search_replace_values(self, spec: Dict[str, Any], search: str, replace: str) -> Dict[str, Any]:
        """Recursively search and replace in a dictionary."""

        if isinstance(spec, list):
            for i, item in enumerate(spec):
                spec[i] = self._search_replace_values(item, search, replace)
            return spec

        if not isinstance(spec, dict):
            return spec

        for key, value in spec.items():
            if isinstance(value, str) and search in value:
                spec[key] = value.replace(search, replace)
            else:
                spec[key] = self._search_replace_values(value, search, replace)

        return spec

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by restructuring prefix variants."""
        if path is None:
            path = []
            
        if not isinstance(spec, dict):
            return spec

        # Focus on components/schemas section
        if len(path) >= 2 and path[-2] == 'components' and path[-1] == 'schemas':

            names_to_pop = []
            for name, schema in spec.items():

                concrete_name = self._find_concrete_type(name, schema)
                if not concrete_name:
                    # If no concrete type is found, skip this schema
                    continue

                concrete_schema = spec.get(concrete_name)

                if 'allOf' not in concrete_schema:
                    concrete_schema['allOf'] = []

                for item in schema.get('allOf', []):
                    if item['$ref'] != f"#/components/schemas/{concrete_name}":
                        concrete_schema['allOf'].append(item)

                if 'type' in concrete_schema and concrete_schema['type'] == 'object':
                    concrete_schema.pop('type')

                names_to_pop.append(name)

                self.search_replace.append({
                    'search': f"#/components/schemas/{name}",
                    'replace': f"#/components/schemas/{concrete_name}"
                     })

            for item in names_to_pop:
                self.stats.counts['components_removed'] += 1
                spec.pop(item)

            return spec

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key])
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key]) if isinstance(item, dict) else item 
                            for item in value]

        return spec

    def post_clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:

        for search_replace in self.search_replace:
           spec = self._search_replace_values(spec, search_replace['search'], search_replace['replace'])

        self.search_replace = []

        return spec
