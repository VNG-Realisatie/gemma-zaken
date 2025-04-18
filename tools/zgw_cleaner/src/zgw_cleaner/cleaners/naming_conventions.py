from typing import Dict, Any
from ..cleaner import Cleaner
from caseconverter import snakecase, camelcase, pascalcase

class NamingConventionsCleaner(Cleaner):
    """Removes redundant allOf constructs with single references."""
    
    def __init__(self):
        super().__init__('naming-conventions')
        self.field_name_mapping = {
            # Rationale: even though headers are case-insensitive,
            # for consistency, we follow the convention of HTTP headers.
            # (kebab-case with capitalized words)
            #
            # Associated Spectral rule: missing-version-header
            'API-version': 'API-Version'
        }

        self.search_replace_list = []


    def _pascal_case(self, name: str) -> str:
        return ''.join(word.capitalize() for word in name.split('_'))

    def clean(self, spec: Dict[str, Any], root_spec: Dict[str, Any] = None, path: list = []) -> Dict[str, Any]:
        """Cleans the OpenAPI spec by renaming fields."""

        if root_spec is None:
            root_spec = spec

        #
        # objectIdentificatie: $ref: '#/components/schemas/AdresObject'
        # to 
        # objectIdentificatie: $ref: '#/components/schemas/AdresIdentificatie'
        #
        if len(path)>0 and path[-1] == 'objectIdentificatie' and isinstance(spec, dict) and '$ref' in spec and spec['$ref'].endswith('Object'):
            key = spec['$ref'].split('/')[-1]
            if key in root_spec['components']['schemas']:
                base_name = key[:-6]
                self.search_replace_list.append([key, base_name + 'Identificatie'])

        #
        # betrokkeneIdentificatie: $ref: '#/components/schemas/RolMedewerker'
        # to 
        # betrokkeneIdentificatie: $ref: '#/components/schemas/MedewerkerIdentificatie'
        #
        if len(path)>0 and path[-1] == 'betrokkeneIdentificatie' and isinstance(spec, dict) and '$ref' in spec and spec['$ref'].startswith('#/components/schemas/Rol'):
            key = spec['$ref'].split('/')[-1]
            if key in root_spec['components']['schemas']:
                base_name = key[3:]
                self.search_replace_list.append([key, base_name + 'Identificatie'])

        #
        # medewerker_Rol:
        # to
        # MedewerkerRol:
        #
        if len(path)>0 and path[-1] == 'RolVariant':
            for item in spec['oneOf']:
                key = item['$ref'].split('/')[-1]
                if key.endswith('_Rol'):
                    base_name = key[:-4].replace('_', ' ')
                    base_name = pascalcase(base_name) + 'Rol'
                    self.search_replace_list.append([key, base_name])

        #
        # adres_ZaakObject:
        # to
        # AdresZaakObject:
        #
        #print(path)#
        if len(path)>0 and path[-1] == 'ZaakObjectVariant':

            for item in spec['oneOf']:
                key = item['$ref'].split('/')[-1]
                if key.endswith('_ZaakObject'):


                    base_name = key[:-11].replace('_', ' ')
                    base_name = pascalcase(base_name) + 'ZaakObject'
                    self.search_replace_list.append([key, base_name])


        if path == ['components', 'schemas']:

            last_item_to_front_pascalcase = []
            remove_object_prefix = []

            for key, value in spec.items():

                if camelcase(key) == key:
                    self.search_replace_list.append([key, pascalcase(key)])

                # Rationale: in current OpenAPI spec, allOf constructs are used to compose the types
                # currently in the variants (oneOf-constructs). E.g., a ZaakObject is a base class
                # for all concrete ZaakObject variants. To make this clear, we rename the base class to
                # ZaakObjectBase (for example).
                if key.endswith('Variant'):
                    base_name = key[:-7]
                    if base_name in spec:
                        self.search_replace_list.append([base_name,base_name + 'Base'])

                if key.startswith('Object') and not key.endswith('Base') and not key.endswith('Variant') and key != 'ObjectTypeEnum':
                    if key.endswith('Enum'):
                        remove_object_prefix.append(key)
                    else:
                        last_item_to_front_pascalcase.append(key)


            for key in last_item_to_front_pascalcase:
                new_name = key[len('Object'):] + 'Object'
                root_spec = self._rename_component(key, new_name, root_spec)

            for key in remove_object_prefix:
                new_name = key[len('Object'):]
                root_spec = self._rename_component(key, new_name, root_spec)

        if isinstance(spec, dict):
            for old_name, new_name in self.field_name_mapping.items():
                if old_name in spec:
                    ref = spec[old_name]
                    spec.pop(old_name)
                    spec[new_name] = ref
                    self.stats.counts['field_renames'] += 1                

            # Recurse through nested structures with path tracking
            for key, value in spec.items():
                new_path = path + [key]
                spec[key] = self.clean(value, root_spec, new_path)
                
        elif isinstance(spec, list):
            return [self.clean(item, root_spec, path) for item in spec]

        return spec


    def post_clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:

        for item in self.search_replace_list:
            spec = self._rename_component(item[0], item[1], spec)

        self.search_replace_list = []

        return spec

