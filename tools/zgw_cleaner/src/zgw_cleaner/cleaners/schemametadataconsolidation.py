from typing import Dict, Any
from copy import deepcopy
from ..core import Cleaner
import logging

class SchemaMetadataConsolidationCleaner(Cleaner):
    """
    Consolidates schema metadata by moving property-level metadata to the referenced schema definition
    when appropriate.
    """
    
    def _get_ref_schema(self, spec_root: Dict, ref: str) -> Dict:
        """Gets the referenced schema from the components section."""
        if not ref.startswith('#/components/schemas/'):
            return None
        schema_name = ref.split('/')[-1]
        return spec_root.get('components', {}).get('schemas', {}).get(schema_name)

    def _consolidate_property(self, property_def: Dict, ref_schema: Dict) -> Dict:
        """Consolidates metadata from property into referenced schema."""
        metadata_fields = ['description', 'title']
        
        # Don't modify if there's no reference schema
        if not ref_schema:
            return property_def
            
        # Copy metadata to referenced schema if not present
        for field in metadata_fields:
            if field in property_def and field not in ref_schema:
                ref_schema[field] = property_def[field]
                del property_def[field]
                self.stats.counts['fields_moved'] = self.stats.counts.get('fields_moved', 0) + 1

            if field in property_def and field in ref_schema and property_def[field] != ref_schema[field]:
                self.stats.counts['fields_conflict'] = self.stats.counts.get('fields_conflict', 0) + 1
                logging.debug(f"Conflict in {field} for {property_def} and {ref_schema}")
                
            if field in property_def and field in ref_schema and property_def[field] == ref_schema[field]:
                del property_def[field]
                self.stats.counts['fields_deleted'] = self.stats.counts.get('fields_deleted', 0) + 1
                
        return property_def

    def clean(self, spec: Dict[str, Any], spec_root: Dict[str, Any] = None) -> Dict[str, Any]:
        """Clean the specification by consolidating schema metadata."""
        if spec_root is None:
            spec_root = spec

        if not isinstance(spec, dict):
            return spec
        
        if len(spec) == 1:
            return spec

        # Process properties that use allOf with a single ref
        if 'allOf' in spec and len(spec['allOf']) == 1:
            ref = spec['allOf'][0].get('$ref')
            if ref:
                ref_schema = self._get_ref_schema(spec_root, ref)
                if ref_schema:
                    spec = self._consolidate_property(spec, ref_schema)

        # Process properties that have a single ref
        if '$ref' in spec:
            ref = spec['$ref']
            ref_schema = self._get_ref_schema(spec_root, ref)
            if ref_schema:
                spec = self._consolidate_property(spec, ref_schema)

        # Recurse through nested structures
        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                spec[key] = self.clean(value, spec_root)

        return spec
