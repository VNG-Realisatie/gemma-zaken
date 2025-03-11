from pathlib import Path
from typing import Dict, List
from ruamel.yaml import YAML
from .validators.spectral import SpectralValidator
from .validators.zgw_cleaner import ZgwCleanerValidator

class ToolsValidator:
    def __init__(self, specs_dir: Path, spectral_ruleset: Path = None):
        self.specs_dir = specs_dir
        self.yaml = YAML()
        self.spectral = SpectralValidator(spectral_ruleset)
        self.cleaner = ZgwCleanerValidator('..')

    def load_specs(self, yaml_file: Path) -> List[Dict]:
        """Load multiple YAML documents from a file."""
        with yaml_file.open() as f:
            return list(self.yaml.load_all(f))

    def validate_all(self) -> bool:
        """Validate all specs in the directory."""
        success = True
        for yaml_file in self.specs_dir.glob("*.yaml"):
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
                print(f"Warning: Spec in {yaml_file} missing x-tools-validator.id")
                continue
                
            # Validate against Spectral
            if 'spectral' in validator_info:
                self.spectral.validate_spec(spec)

            # Validate cleaner if linked
            if cleaner_id := validator_info.get('cleaner-result'):
                cleaned_spec = self.cleaner.clean(spec)
                # TODO: Implement comparison with the referenced clean result
                
        return success
