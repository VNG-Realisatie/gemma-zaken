from typing import Dict, Any
from ..cleaner import Cleaner
from copy import deepcopy

class TagsCleaner(Cleaner):
    """Collects operation tags and adds them to global tags section."""
    
    def __init__(self):
        super().__init__()
        self.collected_tags = set()

    def _collect_tags(self, spec: Dict[str, Any]) -> None:
        """Collect all operation tags."""
        if 'paths' in spec:
            for path in spec['paths'].values():
                for operation in path.values():
                    if 'tags' in operation:
                        self.collected_tags.update(operation['tags'])

    def _add_tags_to_global(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Add collected tags to global tags section."""
        if not self.collected_tags:
            return spec

        if 'tags' not in spec:
            spec['tags'] = []

        # Get existing tag names
        existing_tags = {tag['name'] for tag in spec['tags']} if spec['tags'] else set()

        # Add missing tags
        for tag in self.collected_tags:
            if tag not in existing_tags:
                spec['tags'].append({
                    'name': tag,
                    'description': 'TODO: voeg beschrijving toe'
                })
                self.stats.counts['tags_added'] = self.stats.counts.get('tags_added', 0) + 1

        return spec

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Clean the specification by consolidating tags."""
        if not isinstance(spec, dict):
            return spec

        # First pass: collect all tags
        self._collect_tags(spec)
        
        # Second pass: add missing tags to global section
        spec = self._add_tags_to_global(spec)

        return spec
