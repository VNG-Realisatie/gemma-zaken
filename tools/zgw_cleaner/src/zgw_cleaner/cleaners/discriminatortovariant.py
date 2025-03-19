from typing import Dict, Any
from ..cleaner import Cleaner

class DiscriminatorToVariantCleaner(Cleaner):

    def _has_discriminator_without_variant(self, schema: Dict[str, Any]) -> bool:
        """Check if schema has a discriminator that needs to be transformed into a variant type"""
        return (isinstance(schema, dict) 
                and 'discriminator' in schema 
                and 'oneOf' not in schema)

    def _create_variant_name(self, original_name: str) -> str:
        name = original_name
        if name.lower().endswith('base'):
            name = name[:-4]
        return "{name}Variant".format(name=name)

    def _create_property_name(self, original_name: str) -> str:
        name = original_name
        if name.lower().endswith('type'):
            return name[:-4]
        return name

    def _create_variant_schema(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Extract discriminator-related parts into a variant schema.
        Returns (variant_schema, remaining_schema)"""
        
        # Extract discriminator and its property
        discriminator = schema['discriminator']
        if not 'mapping' in discriminator:
            return schema

        property_name = discriminator['propertyName']
        data_name = self._create_property_name(property_name)
        
        properties = schema.get('properties', {})
        discriminator_property = properties[property_name]
        
        # Build oneOf and mapping from enum values
        one_of = []
        
        # Try to use a mapping if it's available
        mapping = discriminator.get('mapping', {})
        for value, ref in mapping.items():

            one_of_object = {
                #'type': 'object',
                'properties': {
                    'type': {
                        'type': 'string',
                        'enum': [value]
                    },
                    'value': {
                        '$ref': ref
                    }
                },
            }
            one_of.append(one_of_object)

        variant = {
            'type': 'object',
            'required': ['type', 'value'],
            'additionalProperties': False,
            # 'discriminator': {
            #     'propertyName': 'type',
            #     'mapping': mapping.copy()
            # },
            'oneOf': one_of,
        }

        # Return the variant schema object
        return variant

    def _add_discriminator_mapping(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Update the original schema to use the variant schema for discriminator"""

        if 'discriminator' not in schema:
            return schema

        discriminator = schema['discriminator']
        if 'mapping' in discriminator:
            return schema
        
        if 'propertyName' not in discriminator:
            return schema

        property_name = discriminator['propertyName']
        properties = schema.get('properties', {})
        discriminator_property = properties[property_name]

        if 'enum' not in discriminator_property:
            return schema
        
        enum_values = discriminator_property.get('enum', [])
        if len(enum_values) == 0:
            return schema

        discriminator['mapping'] = {}

        for value in enum_values:
            discriminator['mapping'][value] = f"#/components/schemas/{value}"
        
        return schema

    def _add_property_name_to_required(self, schema: Dict[str, Any]) -> Dict[str, Any]:

        if 'discriminator' not in schema:
            return schema
        
        discriminator = schema['discriminator']
        if 'propertyName' not in discriminator:
            return schema

        property_name = discriminator['propertyName']

        if 'required' not in schema:
            schema['required'] = [property_name]
        elif property_name not in schema['required']:
            schema['required'].append(property_name)

        return schema

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

                # Add discriminator mapping to the schema
                schema = self._add_discriminator_mapping(schema)
                schema = self._add_property_name_to_required(schema)

                variant_name = self._create_variant_name(name)
                variant = self._create_variant_schema(schema)
                schemas[variant_name] = variant

                # Update refs throughout the spec, except in allOf
                spec = self._update_refs(spec, name, variant_name)




        return spec
    