from typing import Dict, Any
from ..core import Cleaner

class FieldNameCleaner(Cleaner):
    """Removes redundant allOf constructs with single references."""
    
    def __init__(self):
        super().__init__()
        self.field_name_mapping = {
            # Rationale: even though headers are case-insensitive,
            # for consistency, we follow the convention of HTTP headers.
            # (kebab-case with capitalized words)
            #
            # Associated Spectral rule: missing-version-header
            'API-version': 'API-Version'
        }

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Cleans the OpenAPI spec by renaming fields."""

        if isinstance(spec, dict):
            for old_name, new_name in self.field_name_mapping.items():
                if old_name in spec:
                    ref = spec[old_name]
                    spec.pop(old_name)
                    spec[new_name] = ref
                    self.stats.counts['field_renames'] += 1                

            # Recurse through nested structures
            for key, value in spec.items():
                spec[key] = self.clean(value)
                
        elif isinstance(spec, list):
            return [self.clean(item) for item in spec]

        return spec
