from typing import Dict, Any, Tuple
from ..core import Cleaner

class EnumDescriptionsCleaner(Cleaner):
    """Extracts enum descriptions from description fields and moves them to x-enumDescriptions."""
    
    def _parse_enum_descriptions(self, description: str) -> Tuple[dict, str]:
        """Parse enum descriptions and return cleaned description."""
        if 'Uitleg bij mogelijke waarden:' not in description:
            return {}, description

        enum_descriptions = {}
        clean_lines = []
        in_descriptions = False
        
        for line in description.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line == 'Uitleg bij mogelijke waarden:':
                in_descriptions = True
                continue
                
            if not in_descriptions:
                clean_lines.append(line)
            elif line.startswith('*'):
                parts = line.split('`')
                if len(parts) >= 3:
                    key = parts[1]
                    value = parts[2].split('-', 1)[1].strip()
                    enum_descriptions[key] = value
                    
        return enum_descriptions, ' '.join(clean_lines).strip()

    def _process_schema(self, schema: Dict[str, Any]) -> None:
        """Recursively process schema objects to extract enum descriptions."""
        if not isinstance(schema, dict):
            return

        # Extract enum descriptions
        if 'enum' in schema and 'description' in schema:
            enum_descriptions, clean_description = self._parse_enum_descriptions(schema['description'])
            if enum_descriptions:
                schema['x-enumDescriptions'] = enum_descriptions
                schema['description'] = clean_description
                self.stats.counts['enum_descriptions_extracted'] += 1

        # Recurse through all possible schema locations
        for key, value in schema.items():
            if isinstance(value, dict):
                self._process_schema(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._process_schema(item)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Clean the specification by extracting enum descriptions."""
        if not isinstance(spec, dict):
            return spec

        self.stats.counts['enum_descriptions_extracted'] = 0
        self._process_schema(spec)
        return spec
