from typing import Dict, Any, List
from ..cleaner import Cleaner

class RedundantTitleCleaner(Cleaner):
    """
    Removes redundant titles that match the property/schema name or add no value.
    """
    
    def _should_remove_title(self, name: str, title: str) -> bool:
        """Determines if a title should be removed based on its value and context."""
        if not title or not isinstance(title, str):
            return False
            
        # Case insensitive comparison, strip spaces and underscores
        # Examples:
        #   applicatieId         <-> ApplicatieId
        #   'Geometrie  '        <-> geometrie
        #   subAdresBuitenland_1 <-> sub adres buitenland 1
        # 
        # Note: This will also match any combination of the above
        #
        name_clean = name.replace('_', '').replace(' ', '').lower()
        title_clean = title.replace('_', '').replace(' ', '').lower()        
        if name_clean == title_clean:
            return True

        return False

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        """Clean the specification by removing redundant titles."""
        if path is None:
            path = []
            
        if not isinstance(spec, dict):
            return spec

        # Case 1: Property name matches title
        if len(path) >= 2 and path[-2] == 'properties' and 'title' in spec:
            property_name = path[-1]
            if self._should_remove_title(property_name, spec['title']):
                del spec['title']
                self.stats.counts['titles_removed'] = self.stats.counts.get('titles_removed', 0) + 1

        # Case 2: Parameter name matches schema title
        if 'name' in spec and 'schema' in spec and isinstance(spec['schema'], dict):
            if 'title' in spec['schema']:
                if self._should_remove_title(spec['name'], spec['schema']['title']):
                    del spec['schema']['title']
                    self.stats.counts['titles_removed'] = self.stats.counts.get('titles_removed', 0) + 1

        # Case 3: Schema name in components matches title
        if len(path) >= 3 and path[-3] == 'components' and path[-2] == 'schemas' and 'title' in spec:
            schema_name = path[-1]
            if self._should_remove_title(schema_name, spec['title']):
                del spec['title']
                self.stats.counts['titles_removed'] = self.stats.counts.get('titles_removed', 0) + 1

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, dict):
                spec[key] = self.clean(value, path + [key])
            elif isinstance(value, list):
                spec[key] = [self.clean(item, path + [key]) if isinstance(item, dict) else item 
                            for item in value]

        return spec
