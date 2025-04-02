from typing import Dict, Any, List
from ..cleaner import Cleaner

class SortCleaner(Cleaner):
    """Sorts OpenAPI specification fields in a predetermined order.
    """
    
    def __init__(self):
        super().__init__('sort-fields')

    def _is_schema(self, obj: Dict[str, Any], path: List[str]) -> bool:
        """
        Determines if the object is a schema by checking its location and contents.
        """
        # Direct schema locations
        schema_paths = [
            ['components', 'schemas'],
            ['definitions'],  # OpenAPI 2.0
            ['info']
        ]
        
        # Check if we're in a schema location
        for schema_path in schema_paths:
            if path[:len(schema_path)] == schema_path:
                return True
                
        # Check if it has schema-like properties
        schema_indicators = {'type', 'properties', 'allOf', 'anyOf', 'oneOf', 'items'}
        return bool(set(obj.keys()) & schema_indicators)

    def _sort_schema(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sorts a schema according to preferred field ordering.
        """
        def key_ordering(key: str) -> int:
            order = {
                'allOf': 0,
                'anyOf': 1,
                'oneOf': 2,
                'title': 3,
                'version': 4,
                'description': 5,
                'type': 6,
                'items': 7,
                'properties': 8,
                'format': 9,
                'required': 10,
                'example': 11,
            }
            return order.get(key, 100)  # unspecified keys go to the end

        return dict(sorted(schema.items(), key=lambda item: key_ordering(item[0])))

    def _sort_responses(self, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sorts responses in order: 2XX, 3XX, 4XX, 5XX, default
        This happens to be the same order as a lexicographical sort.
        """
        return dict(sorted(responses.items()))

    def _sort_root(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sorts the root of an OpenAPI document
        """
        def key_ordering(key: str) -> int:
            order = {
                "openapi": 0,
                "info": 1,
                "servers": 2,
                "security": 3,
                "paths": 4,
                "components": 5,
                "tags": 6,
                "externalDocs": 7
            }
            return order.get(key, 100)  # unspecified keys go to the end

        return dict(sorted(schema.items(), key=lambda item: key_ordering(item[0])))

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        if path is None:
            path = []

        if not isinstance(spec, dict):
            return spec

        # Determine which sorting to apply based on the path and content
        if self._is_schema(spec, path):
            spec = self._sort_schema(spec)
        elif 'responses' in path[-1:]:
            spec = self._sort_responses(spec)
            
        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                spec[key] = self.clean(value, path + [key])

        if path == []:
            spec = self._sort_root(spec)

        return spec

