from pathlib import Path
from typing import Dict, List
from ruamel.yaml import YAML
from .validators.spectral import SpectralValidator
from .validators.zgw_cleaner import ZgwCleanerValidator

class ToolsValidator:
    def __init__(self, test_cases_dir: Path, spectral_ruleset: Path = None):
        self.test_cases_dir = test_cases_dir
        self.yaml = YAML()
        self.spectral = SpectralValidator(spectral_ruleset)
        self.cleaner = ZgwCleanerValidator()

    def load_specs(self, yaml_file: Path) -> List[Dict]:
        """Load multiple YAML documents from a file."""
        with yaml_file.open() as f:
            return list(self.yaml.load_all(f))

    def validate_all(self) -> bool:
        """Validate all specs in the directory."""
        success = True
        for yaml_file in self.test_cases_dir.glob("*.yaml"):
            if not self.validate_file(yaml_file):
                success = False
        return success

    def validate_file(self, yaml_file: Path) -> bool:
        """Validate a single YAML file."""
        specs = self.load_specs(yaml_file)
        success = True

        for spec in specs:
            validator_info = spec.get('x-tools-validator', {})
            spec_id = validator_info.get('id')
            if not spec_id:
                print(f"Error: Spec in {yaml_file} missing x-tools-validator.id")
                return False

        specs_map = {spec['x-tools-validator']['id']: spec for spec in specs}

        for spec_id, spec in specs_map.items():
            validator_info = spec.get('x-tools-validator', {})

            # Validate against Spectral
            if 'spectral' in validator_info:
                self.spectral.validate_spec(spec)

            # Validate cleaner if linked
            if 'zgw-cleaner' in validator_info:
                if not 'should-clean-to' in validator_info['zgw-cleaner']:
                    print(f"Error: Spec {spec_id} has cleaner but no should-clean-to")
                    return False

                cleaned_id = validator_info['zgw-cleaner']['should-clean-to']
                cleaned_spec = self.cleaner.clean(spec)
                clean_ref = specs_map.get(cleaned_id)

                if not self.cleaner.compare_specs(cleaned_spec, clean_ref):
                    print(f"  zgw-cleaner-should-clean-to {cleaned_id}: ✗ FAIL")
                else:
                    print(f"  zgw-cleaner-should-clean-to {cleaned_id}: ✓ PASS")

        return success
