from typing import Dict, Any
from ..cleaner import Cleaner

class StandalonexOfCleaner(Cleaner):
    """Removes redundant allOf constructs with single references.
    
       Associated Spectral rule: redundant-allof"""
    
    def __init__(self):
        super().__init__('no-standalone-xof')
   
    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(spec, dict):
            for xOf in [ 'allOf', 'anyOf', 'oneOf' ]:
                while xOf in spec and len(spec) == 1 and len(spec[xOf]) == 1:
                    ref = spec[xOf][0]
                    spec.pop(xOf)
                    spec.update(ref)
                    self.stats.counts[f'{xOf}_replaced_by_refs'] += 1                

            # Recurse through nested structures
            for key, value in spec.items():
                spec[key] = self.clean(value)
                
        elif isinstance(spec, list):
            return [self.clean(item) for item in spec]
            
        return spec
