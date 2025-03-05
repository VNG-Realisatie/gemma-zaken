from typing import Dict, Any
from ..core import Cleaner

class DiscriminatorToVariantCleaner(Cleaner):

    def _has_discriminator_without_variant(self, schema: Dict[str, Any]) -> bool:
        """Check if schema has a discriminator that needs to be transformed into a variant type"""
        return (isinstance(schema, dict) 
                and 'discriminator' in schema 
                and 'oneOf' not in schema)

    def _create_variant_name(self, original_name: str) -> str:
        name = original_name
        if name.endswith('Base'):
            name = name[:-4]
        return "{name}Variant".format(name=name)

    def _extract_variant_parts(self, schema: Dict[str, Any]) -> tuple[Dict[str, Any], Dict[str, Any]]:
        """Extract discriminator-related parts into a variant schema.
        Returns (variant_schema, remaining_schema)"""
        remaining = schema.copy()
        
        # Extract discriminator and its property
        discriminator = remaining.pop('discriminator')
        property_name = discriminator['propertyName']
        
        properties = remaining.get('properties', {})
        discriminator_property = properties.pop(property_name, {})
        
        # Build oneOf and mapping from enum values
        enum_values = discriminator_property.get('enum', [])
        one_of = []
        mapping = {}
        
        for value in enum_values:
            schema_ref = f"#/components/schemas/{value}"
            
            one_of.append({"$ref": schema_ref})
            mapping[value] = schema_ref

        # Build variant schema
        variant = {
            'type': 'object',
            'oneOf': one_of,
            'discriminator': {
                'propertyName': property_name,
                'mapping': mapping
            },
            'properties': {
                property_name: discriminator_property
            },
            'required': [property_name]
        }
        
        # Clean up remaining schema
        if properties:
            remaining['properties'] = properties
        else:
            remaining.pop('properties', None)
            
        if 'required' in remaining and property_name in remaining['required']:
            remaining['required'].remove(property_name)
            if not remaining['required']:
                remaining.pop('required')

        return variant, remaining
    
    def _should_update_ref(self, parent: Dict[str, Any], ref: str) -> bool:
        """Determine if this reference should be updated to point to variant"""
        # Don't update refs in allOf
        if parent.get('allOf') and ref in [r.get('$ref') for r in parent['allOf']]:
            return False
        return True

    def _update_refs(self, schema: Dict[str, Any], original_name: str, variant_name: str, parent: Dict[str, Any] = None) -> Dict[str, Any]:
        """Update references to point to variant type, except in allOf"""
        if isinstance(schema, dict):
            if '$ref' in schema and isinstance(schema['$ref'], str):
                ref = schema['$ref']
                if ref == f'#/components/schemas/{original_name}':
                    if parent is None or self._should_update_ref(parent, ref):
                        schema['$ref'] = f'#/components/schemas/{variant_name}'
            
            for key, value in schema.items():
                if isinstance(value, (dict, list)):
                    self._update_refs(value, original_name, variant_name, schema)
        
        elif isinstance(schema, list):
            for item in schema:
                self._update_refs(item, original_name, variant_name, parent)
                
        return schema

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        if 'components' not in spec or 'schemas' not in spec['components']:
            return spec

        schemas = spec['components']['schemas']
        
        for name, schema in list(schemas.items()):
            if self._has_discriminator_without_variant(schema):
                variant_name = self._create_variant_name(name)
                variant, remaining = self._extract_variant_parts(schema)
                
                schemas[variant_name] = variant
                schemas[name] = remaining

                # Update refs throughout the spec, except in allOf
                spec = self._update_refs(spec, name, variant_name)

        return spec
    