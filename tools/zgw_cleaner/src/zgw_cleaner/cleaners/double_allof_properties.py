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

            # New case: if the schema only has allOf, and one of the allOf items defines schema keywords directly
            # (e.g., properties, required, description), lift those to the parent schema level and remove that item.
            if set(spec.keys()) == {'allOf'} and isinstance(spec.get('allOf'), list):
                allowed_lift_keys = {
                    'properties', 'required', 'type', 'description', 'title', 'deprecated', 'readOnly', 'writeOnly',
                    'nullable', 'default', 'example', 'examples', 'format', 'enum', 'multipleOf', 'maximum',
                    'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems',
                    'minItems', 'uniqueItems', 'maxProperties', 'minProperties', 'additionalProperties'
                }
                lifted_parent: Dict[str, Any] = {}
                remaining_allof = []
                for item in spec['allOf']:
                    if isinstance(item, dict) and set(item.keys()).issubset(allowed_lift_keys):
                        # Merge properties
                        if 'properties' in item and isinstance(item['properties'], dict) and item['properties']:
                            lifted_parent.setdefault('properties', {})
                            lifted_parent['properties'].update(item['properties'])
                        # Merge required
                        if 'required' in item and isinstance(item['required'], list):
                            lifted_parent.setdefault('required', [])
                            for r in item['required']:
                                if r not in lifted_parent['required']:
                                    lifted_parent['required'].append(r)
                        # Copy over other scalar/schema keywords if not already set
                        for key in allowed_lift_keys - {'properties', 'required'}:
                            if key in item and key not in lifted_parent:
                                lifted_parent[key] = deepcopy(item[key])
                        # Count and skip adding this item back to allOf
                        self.stats.counts['double_allof_properties_merged'] += 1
                        continue
                    remaining_allof.append(item)

                if lifted_parent:
                    for k, v in lifted_parent.items():
                        spec[k] = deepcopy(v)
                    if remaining_allof:
                        spec['allOf'] = remaining_allof
                    else:
                        del spec['allOf']

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