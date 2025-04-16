
from typing import Dict, Any, List
import logging
from copy import deepcopy
from ..cleaner import Cleaner


class RemoveUnusedCleaner(Cleaner):
    """Removes components that aren't referenced anywhere in the specification."""
    
    def __init__(self):
        super().__init__('remove-unused-components')
        self.used_components = set()
   
    def collect_used_components(self, spec: Dict[str, Any]):
        """Recursively collect all $refs in the specification."""
        if isinstance(spec, dict):
            if '$ref' in spec:
                ref = spec['$ref']
                if ref.startswith('#/components/'):
                    # Convert reference path to components path
                    path = ref.replace('#/components/', '').split('/')
                    self.used_components.add(tuple(path))
            
            # Recurse through nested structures
            for value in spec.values():
                self.collect_used_components(value)
                
        elif isinstance(spec, list):
            for item in spec:
                self.collect_used_components(item)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        # Reset refs collection
        self.used_components = set()
        
        # First pass: collect all references
        self.collect_used_components(spec)
        
        # If there's no components section, return original spec
        if 'components' not in spec:
            return spec
            
        # Second pass: remove unused components
        components = spec['components']
        for component_type in list(components.keys()):
            if component_type in components:
                for name in list(components[component_type].keys()):
                    if (component_type, name) not in self.used_components:

                        actual_component = spec['components'][component_type][name]

                        #
                        # Here, we filter on deletion.
                        # * Should have 1 property, e.g., objectIdentificatie
                        # * Should have this property name somehow in its component name
                        #
                        if 'properties' not in actual_component:
                            continue
                        if len(actual_component['properties']) != 1:
                            continue
                        property_key = list(actual_component['properties'].keys())[0].lower()
                        if property_key not in name.replace('_', '').lower():
                            continue

                        del components[component_type][name]
                        self.stats.counts['unused_components_removed'] += 1
                
                # Remove empty component types
                if not components[component_type]:
                    del components[component_type]
                    
        # Remove empty components section
        if not components:
            del spec['components']
            
        return spec
