from typing import Dict, Any, List
import logging
from copy import deepcopy
from ..cleaner import Cleaner
from caseconverter import pascalcase
from ruamel.yaml.scalarstring import SingleQuotedScalarString

class ParameterConsolidationCleaner(Cleaner):

    def __init__(self, param_component_namer=None):
        super().__init__()
        self.param_component_namer = param_component_namer or self._ref_name
        self.param_patterns = {}
        self.param_occurrences = {}

    def _ref_name(self, param_def: Dict) -> str:
        """Generate reference name for a parameter."""
        if 'name' in param_def:
            return pascalcase(param_def['name'].lower().replace('-', '_')) + 'Parameter'
        return "unnamed_param"

    def _create_parameter_key(self, param_def: Dict) -> frozenset:
        if not isinstance(param_def, dict):
            return frozenset()

        key_items = []
        for k, v in param_def.items():
            if isinstance(v, dict):
                v = tuple(sorted((sk, str(sv)) for sk, sv in v.items()))
            key_items.append((k, str(v)))
        return frozenset(key_items)

    def _collect_parameter_patterns(self, spec: Dict[str, Any]):
        if 'paths' not in spec:
            return

        for path_item in spec['paths'].values():
            for operation in path_item.values():
                if 'parameters' not in operation:
                    continue

                for param in operation['parameters']:
                    param_key = self._create_parameter_key(param)
                    self.param_occurrences[param_key] = self.param_occurrences.get(param_key, 0) + 1
                    if param_key not in self.param_patterns:
                        self.param_patterns[param_key] = deepcopy(param)

    def _setup_components(self, spec: Dict[str, Any]):
        if 'components' not in spec:
            spec['components'] = {}
        if 'parameters' not in spec['components']:
            spec['components']['parameters'] = {}
        return spec['components']['parameters']

    def _replace_parameters(self, spec: Dict[str, Any]):
        consolidated_params = self._setup_components(spec)
        component_names = {}

        for param_key, count in self.param_occurrences.items():
            if count > 1:
                component_name = self.param_component_namer(self.param_patterns[param_key])
                consolidated_params[component_name] = self.param_patterns[param_key]
                component_names[param_key] = component_name
                self.stats.counts['parameters_consolidated'] = self.stats.counts.get('parameters_consolidated', 0) + 1

        for path_item in spec['paths'].values():
            for operation in path_item.values():
                if 'parameters' not in operation:
                    continue
                new_params = []
                for param in operation['parameters']:
                    param_key = self._create_parameter_key(param)
                    if param_key in component_names:
                        new_params.append({'$ref': f"#/components/parameters/{component_names[param_key]}"})
                        self.stats.counts['parameters_reused'] = self.stats.counts.get('parameters_reused', 0) + 1
                    else:
                        new_params.append(param)
                operation['parameters'] = new_params

    def _consolidate_parameters(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        if 'paths' not in spec:
            return spec

        self._collect_parameter_patterns(spec)
        self._replace_parameters(spec)
        return spec

    def clean(self, spec: Dict[str, Any], path: List[str] = None) -> Dict[str, Any]:
        if path is None:
            path = []
            return self._consolidate_parameters(spec)
        if not isinstance(spec, dict):
            return spec

        for key, value in spec.items():
            if isinstance(value, (dict, list)):
                spec[key] = self.clean(value, path + [key])

        return spec
