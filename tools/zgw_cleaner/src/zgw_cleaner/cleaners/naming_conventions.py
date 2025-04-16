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

    def _pascal_case(self, name: str) -> str:
        return ''.join(word.capitalize() for word in name.split('_'))

    def clean(self, spec: Dict[str, Any], root_spec: Dict[str, Any] = None, path: list = []) -> Dict[str, Any]:
        """Cleans the OpenAPI spec by renaming fields."""

        if root_spec is None:
            root_spec = spec

        if path == ['components', 'schemas']:

            rename_to_pascalcase = []
            rename_to_baseclass = []
            last_item_to_front_pascalcase = []
            remove_object_prefix = []
            search_replace_list = []

            for key, value in spec.items():

                if camelcase(key) == key:
                    rename_to_pascalcase.append(key)

                if key.endswith('Variant'):
                    base_name = key[:-7]
                    if base_name in spec:
                        rename_to_baseclass.append(base_name)

                if key.startswith('Object') and not key.endswith('Base') and not key.endswith('Variant') and key != 'ObjectTypeEnum':
                    if key.endswith('Enum'):
                        remove_object_prefix.append(key)
                    else:
                        last_item_to_front_pascalcase.append(key)

                if key.endswith('_PatchedZaakObject'):
                    concept_snake = key[:-len('_PatchedZaakObject')]
                    concept_pascal = pascalcase(concept_snake)
                    new_key = 'PatchedZaak' + concept_pascal + 'Object'
                    search_replace_list.append([key,new_key])

                if key.endswith('_ZaakObject'):
                    concept_snake = key[:-len('_ZaakObject')]
                    concept_pascal = pascalcase(concept_snake)
                    new_key = 'Zaak' + concept_pascal + 'Object'
                    search_replace_list.append([key,new_key])

            for key in rename_to_pascalcase:
                root_spec = self._rename_component(key, pascalcase(key), root_spec)

            for key in rename_to_baseclass:
                root_spec = self._rename_component(key, key + 'Base', root_spec)

            for key in last_item_to_front_pascalcase:
                new_name = key[len('Object'):] + 'Object'
                root_spec = self._rename_component(key, new_name, root_spec)

            for key in remove_object_prefix:
                new_name = key[len('Object'):]
                root_spec = self._rename_component(key, new_name, root_spec)

            for kv in search_replace_list:
                root_spec = self._rename_component(kv[0], kv[1], root_spec)

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
