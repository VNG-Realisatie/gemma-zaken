from typing import Dict, Any
from ..core import Cleaner
from ruamel.yaml.scalarstring import FoldedScalarString

class DescriptionFormatCleaner(Cleaner):
    """Cleans description fields by removing explicit '\n' newline characters
       and formatting with block scalar indicators."""
    
    def __init__(self):
        super().__init__()

    def needs_cleaning(self, description: str) -> bool:
        """Determines if a description needs cleaning."""
        if isinstance(description, FoldedScalarString):
            return False

        if not isinstance(description, str):
            return False
            
        description = description.strip()

        if description.count('\n') < 1 and description.count('\\n') < 1:
            return False

        # Skip if no explicit newlines to clean
        #if '\\n' not in description:
        #    return False
            
        #print(description)
        #print("------------------------------------")

        return True

    def clean_description(self, description: str) -> str:
        """Cleans a single description string."""

        # Replace explicit newlines with actual newlines
        cleaned = description.replace('\\n', '\n')

        # Replace too many newlines with fewer newlines
        cleaned = cleaned.replace('\n\n\n', '\n\n')

        # Split into paragraphs and trim whitespace
        paragraphs = [p.strip() for p in cleaned.split('\n\n')]
        
        # Remove empty paragraphs and join with double newlines
        cleaned = '\n\n'.join(p for p in paragraphs if p)

        return FoldedScalarString(cleaned)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Cleans the OpenAPI spec by reformatting description fields."""
        
        if isinstance(spec, dict):
            # Process description field if present
            if 'description' in spec and self.needs_cleaning(spec['description']):
                original = spec['description']
                cleaned = self.clean_description(original)
                
                #print(cleaned)

                spec['description'] = cleaned
                self.stats.counts['descriptions_cleaned'] = \
                    self.stats.counts.get('descriptions_cleaned', 0) + 1

            # Recurse through nested structures
            for key, value in spec.items():
                spec[key] = self.clean(value)
                
        elif isinstance(spec, list):
            return [self.clean(item) for item in spec]

        return spec
