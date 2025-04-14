from typing import Dict, Any, List
from ..cleaner import Cleaner

class RemoveDiscriminatorCleaner(Cleaner):


    def _try_remove_discriminator(self, spec: Dict[str, Any], root_spec: Dict[str, Any]) -> Dict[str, Any]:

        if 'discriminator' not in spec:
            return spec

        if 'properties' not in spec:
            return spec

        propertyName = spec['discriminator'].get('propertyName', None)
        if propertyName == None:
            return spec
 
        discriminator_property = spec['properties'].get(propertyName, None)
        if discriminator_property == None:
            return spec

        mapping = spec['discriminator'].get('mapping', None)
        if mapping is None:
            return spec

        if 'enum' not in discriminator_property:
            return spec
        if 'x-enumDescriptions' not in discriminator_property:
            return spec

        for enum_value, ref in mapping.items():
            target_component = root_spec['components']['schemas'][ref.split('/')[-1]]
            if 'properties' not in target_component:
                continue
            if propertyName not in target_component['properties']:
                continue
            target_component['properties'][propertyName]['x-enumDescriptions'] = { enum_value: discriminator_property['x-enumDescriptions'][enum_value] } 

        del discriminator_property['x-enumDescriptions']
        del discriminator_property['enum']
        del spec['discriminator']

        self.stats.counts['discriminators_removed'] = self.stats.counts.get('discriminators_removed', 0) + 1
        return spec

    def clean(self, spec: Dict[str, Any], path: List[str] = None, root_spec = None) -> Dict[str, Any]:
        """Clean the specification by removing the discriminator keyword."""
        if path is None:
            path = []
        if root_spec is None:
            root_spec = spec
            
        if not isinstance(spec, dict):
            return spec

        # We should check if there's a oneOf-related equivalent before removing the discriminator
        # For now, we'll just remove it if it exists
        spec = self._try_remove_discriminator(spec, root_spec)

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key], root_spec)
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key], root_spec) if isinstance(item, dict) else item 
                            for item in value]

        return spec
