
from typing import Dict, Any
from collections import Counter, OrderedDict

class CleanerStats:
    """Statistics for a cleaning operation."""
    def __init__(self, name: str):
        self.name = name
        self.counts = Counter()

    def __str__(self):
        if not self.counts:
            return f"{self.name}: no changes made"
        return f"{self.name}: " + ", ".join(f"{k}: {v}" for k, v in self.counts.items())

    def hit(self):
        return self.counts
    
    def miss(self):
        return not self.counts

class Cleaner:
    """Base class for cleanup operations."""
    def __init__(self, cleaner_name=None):
        if cleaner_name is None:
            cleaner_name = self.__class__.__name__
        self.stats = CleanerStats(cleaner_name)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def post_clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        return spec

    def _is_mixin_schema(self, schema: Dict[str, Any]) -> bool:
        """
        Checks if the schema is a mixin schema.
        """
        only_allof = len(schema) == 2 and 'allOf' in schema and 'type' in schema and schema['type'] == 'object'
        only_allof = only_allof or len(schema) == 1 and 'allOf' in schema
        if not only_allof:
            return False
        
        if not isinstance(schema['allOf'], list):
            return False

        # Should be all refs
        for item in schema['allOf']:
            if not isinstance(item, dict) or '$ref' not in item:
                return False

        return True

    def _update_references(self, old_ref: str, new_ref: str, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Updates all references to a component."""
        if isinstance(spec, dict):
            for key, value in spec.items():
                if value == old_ref:
                    spec[key] = new_ref
                    self.stats.counts['reference_updates'] += 1
                else:
                    spec[key] = self._update_references(old_ref, new_ref, value)
        elif isinstance(spec, list):
            return [self._update_references(old_ref, new_ref, item) for item in spec]
        return spec

    def _rename_component(self, old_name: str, new_name: str, spec: Dict[str, Any]) -> Dict[str, Any]:
       
       """Renames a component and updates all references to it."""
       if 'components' in spec:
            components = spec['components']
            for component_type in components:
                if component_type in ['schemas', 'parameters', 'headers']:
                    if old_name in components[component_type]:
                        components[component_type][new_name] = components[component_type].pop(old_name)
                        self.stats.counts['component_renames'] += 1

                        old_ref = f'#/components/{component_type}/{old_name}'
                        new_ref = f'#/components/{component_type}/{new_name}'
                        spec = self._update_references(old_ref, new_ref, spec)
       return spec

