
from typing import Dict, Any
import logging
from ..cleaner import Cleaner
from copy import deepcopy


class DoubleAllOfPropertiesCleaner(Cleaner):
    """Merges properties from allOf references into the main schema when possible."""
    
    def __init__(self):
        super().__init__('double-allof-properties')
   
    def clean(self, spec: Dict[str, Any], root_spec: Dict[str, Any] = None) -> Dict[str, Any]:

        if root_spec is None:
            root_spec = spec

        if isinstance(spec, dict):

            if 'allOf' in spec and len(spec['allOf']) > 1 and 'properties' in spec:

                # Find any allOf items that only contain properties
                properties_to_merge = {}
                new_allOf = []
                
                for item in spec['allOf']:
                    if isinstance(item, dict) and len(item) == 1 and '$ref' in item:
                        related_component = root_spec['components']['schemas'][item['$ref'].split('/')[-1]]
                        if 'properties' in related_component and \
                           (len(related_component) == 1 or (len(related_component) == 2 and 'type' in related_component)):
                           if len(related_component['properties']) == 1:
                                properties_to_merge.update(related_component['properties'])
                                self.stats.counts['double_allof_properties_merged'] += 1
                                continue

                    new_allOf.append(item)
                
                # If we found properties to merge
                if properties_to_merge:
                    # Ensure properties exists in main schema
                    if 'properties' not in spec:
                        spec['properties'] = {}
                    
                    # Merge the properties
                    spec['properties'].update(deepcopy(properties_to_merge))
                    
                    # Update allOf list
                    if new_allOf:
                        spec['allOf'] = new_allOf
                    else:
                        del spec['allOf']
                    
                    self.stats.counts['double_allof_properties_merged'] += 1

            # Recurse through nested structures
            for key, value in spec.items():
                spec[key] = self.clean(value, root_spec)
                
        elif isinstance(spec, list):
            return [self.clean(item, root_spec) for item in spec]
            
        return spec