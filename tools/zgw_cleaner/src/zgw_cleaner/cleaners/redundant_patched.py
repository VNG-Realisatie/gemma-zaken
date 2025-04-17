
from typing import Dict, Any
from ..cleaner import Cleaner
from copy import deepcopy

class RedundantPatchedCleaner(Cleaner):

    def __init__(self):
        super().__init__('redundant-patched')




    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        """Cleans the OpenAPI spec by renaming fields."""

        if 'components' not in spec:
            return spec
        if 'schemas' not in spec['components']:
            return spec

        schemas = spec['components']['schemas']

        if 'PatchedZaakObjectBase' not in schemas:
            return spec
        if 'PatchedZaakObjectVariant' not in schemas:
            return spec
        if 'ZaakObjectVariantBase' in schemas:
            return spec
            
        #spec = self._rename_component('ZaakObjectVariant', 'ZaakObjectVariantBase', spec)

        schemas['ZaakObjectVariantBase'] = deepcopy(schemas['ZaakObjectVariant'])
        del schemas['ZaakObjectVariant']['oneOf']

        schemas['ZaakObjectVariant'] = { 'allOf': [{'$ref': '#/components/schemas/ZaakObjectVariantBase'}]}
        schemas['ZaakObjectVariant']['required'] = deepcopy(schemas['ZaakObjectBase']['required'])
        schemas['ZaakObjectVariant']['properties'] = { '_expand': deepcopy(schemas['ZaakObjectBase']['properties']['_expand'])}

        patched_items = deepcopy(schemas['PatchedZaakObjectVariant']['oneOf'])
        schemas['PatchedZaakObjectVariant'] = { 'allOf': [{'$ref': '#/components/schemas/ZaakObjectVariantBase'}]}
        schemas['PatchedZaakObjectVariant']['required'] = deepcopy(schemas['PatchedZaakObjectBase']['required'])

        del schemas['ZaakObjectBase']['required']
        del schemas['ZaakObjectBase']['properties']['_expand']
        del schemas['PatchedZaakObjectBase']['required']

        check1 = deepcopy(schemas['ZaakObjectBase'])
        check2 = deepcopy(schemas['PatchedZaakObjectBase'])

        del check1['discriminator']
        del check2['discriminator']

        if check1 != check2:
            raise ValueError("Wrong patched comparison!")

        # Alright, now, we can delete most patched items
        for item in patched_items:
            del schemas[item['$ref'].split('/')[-1]]
        del schemas['PatchedZaakObjectBase']
        
        return spec



