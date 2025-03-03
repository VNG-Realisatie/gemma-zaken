from typing import Dict, Any
from ..core import Cleaner

class RedundantAllOfCleaner(Cleaner):
    """Removes redundant allOf constructs with single references."""
    
    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(spec, dict):
            if 'allOf' in spec and len(spec['allOf']) == 1:
                ref = spec['allOf'][0]
                spec.pop('allOf')
                spec.update(ref)
                self.stats.counts['redundant_allof_removed'] += 1                

            # Recurse through nested structures
            for key, value in spec.items():
                spec[key] = self.clean(value)
                
        elif isinstance(spec, list):
            return [self.clean(item) for item in spec]
            
        return spec
