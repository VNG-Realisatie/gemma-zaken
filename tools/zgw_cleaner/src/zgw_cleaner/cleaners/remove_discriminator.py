from typing import Dict, Any, List
from ..cleaner import Cleaner

class RemoveDiscriminatorCleaner(Cleaner):


    def _try_remove_discriminator(self, spec: Dict[str, Any]) -> Dict[str, Any]:

        if 'discriminator' not in spec:
            return spec

        propertyName = spec['discriminator'].get('propertyName', None)

        if propertyName != None and 'properties' in spec and propertyName in spec['properties']:
           discriminator_property = spec['properties'][propertyName]
           if discriminator_property != None:
               if 'enum' in discriminator_property:
                   del discriminator_property['enum']
               if 'x-enumDescriptions' in discriminator_property:
                   del discriminator_property['x-enumDescriptions']

        del spec['discriminator']
        self.stats.counts['discriminators_removed'] = self.stats.counts.get('discriminators_removed', 0) + 1
        return spec

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by removing the discriminator keyword."""
        if path is None:
            path = []
            
        if not isinstance(spec, dict):
            return spec

        # We should check if there's a oneOf-related equivalent before removing the discriminator
        # For now, we'll just remove it if it exists
        spec = self._try_remove_discriminator(spec)

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key])
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key]) if isinstance(item, dict) else item 
                            for item in value]

        return spec
