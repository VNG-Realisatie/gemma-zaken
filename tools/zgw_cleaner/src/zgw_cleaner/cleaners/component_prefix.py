from typing import Dict, Any, List
from ..cleaner import Cleaner

class ComponentPrefixCleaner(Cleaner):
    """
    Restructures component schemas by removing prefix variants and merging with base schemas.
    """
    def __init__(self):
        super().__init__('merge-prefix-components')

    def _find_concrete_type(self, name: str, spec: Dict[str, Any]) -> bool:
        """
        Checks if the schema is a prefix variant that just references the prefixed schema.
        Example: 'zrc' referencing 'zrcAutorisatie'
        """

        if not isinstance(spec, dict) or 'allOf' not in spec:
            return None

        # Should be only allOf
        only_allof = len(spec) == 2 and 'allOf' in spec and 'type' in spec
        only_allof = only_allof or len(spec) == 1 and 'allOf' in spec
        if not only_allof:
            return None

        # Should have exactly two items in allOf
        if not isinstance(spec['allOf'], list):
            return None
        if len(spec['allOf']) != 2:
            return None
        
        # Should be all refs
        refs = []
        for ref in spec['allOf']:
            if not isinstance(ref, dict) or '$ref' not in ref:
                return None
            refs.append(ref['$ref'])

        # Check if one ref points to a schema with name's prefix
        prefix = name.lower()
        for ref in refs:
            short_ref = ref.replace('#/components/schemas/', '')
            if short_ref.startswith(prefix):
                return short_ref

        return None

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by restructuring prefix variants."""
        if path is None:
            path = []
            
        if not isinstance(spec, dict):
            return spec

        # Focus on components/schemas section
        if len(path) >= 2 and path[-2] == 'components' and path[-1] == 'schemas':
            
            items_to_pop = []
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
                            
                items_to_pop.append(name)

            for item in items_to_pop:
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
