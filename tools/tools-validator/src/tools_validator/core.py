from pathlib import Path
from typing import Dict, List
from ruamel.yaml import YAML
from .validators.spectral import SpectralValidator
from .validators.zgw_cleaner import ZgwCleanerValidator
from .validator import ValidationConfig, ValidationResult

def format_result_line(filename: str, test_id: str, spectral_result: bool, cleaner_result: bool) -> str:
    # Truncate filename and test_id if too long
    short_file = filename[:20] + "..." if len(filename) > 23 else filename.ljust(23)
    short_id = test_id[:20] + "..." if len(test_id) > 23 else test_id.ljust(23)
    
    spectral_mark = "✓" if spectral_result else "✗" if spectral_result is not None else "-"
    cleaner_mark = "✓" if cleaner_result else "✗" if cleaner_result is not None else "-"
    
    return f"{short_file} | {short_id} |  {spectral_mark}  |  {cleaner_mark}"

def print_validation_header():
    print("=" * 80)
    print("Filename                | Test ID                 | Spc | Zgw")
    print("-" * 80)

def print_validation_details(name: str, details: List[str]):
    for detail in details:
        print(f"  → {name} {detail}")

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

        print_validation_header()
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

            spectral_result = None
            cleaner_result = None

            # Validate against Spectral
            if 'spectral' in validator_info:
                spectral_config = validator_info['spectral']
                config = ValidationConfig(
                    should_equal=spectral_config.get('should-equal'),
                    should_hit=spectral_config.get('should-hit'),
                    should_miss=spectral_config.get('should-miss')
                )
                spectral_result = self.spectral.run_spectral(spec)
                spectral_result = self.compare_validation_results(config, spectral_result)

            # Validate cleaner if linked
            if 'zgw-cleaner' in validator_info:
                if not 'should-clean-to' in validator_info['zgw-cleaner']:
                    print(f"Error: Spec {spec_id} has cleaner but no should-clean-to")
                    return False

                zgw_cleaner_config = validator_info['zgw-cleaner']
                config = ValidationConfig(
                    should_equal=zgw_cleaner_config.get('should-equal'),
                    should_hit=zgw_cleaner_config.get('should-hit'),
                    should_miss=zgw_cleaner_config.get('should-miss')
                )

                cleaned_spec, cleaner_result = self.cleaner.clean(spec)
                cleaner_result = self.compare_validation_results(config, cleaner_result)

                cleaned_id = validator_info['zgw-cleaner']['should-clean-to']
                clean_ref = specs_map.get(cleaned_id)

                if not self.cleaner.compare_specs(cleaned_spec, clean_ref):
                    cleaner_result.success = False
                    cleaner_result.details.append(f"should clean to {cleaned_id}")

            print(format_result_line(
                yaml_file.name,
                spec_id,
                spectral_result.success if spectral_result else None,
                cleaner_result.success if cleaner_result else None
            ))
            
            # Print details if there are any validation failures
            if spectral_result and spectral_result.details:
                print_validation_details('spectral', spectral_result.details)
            if cleaner_result and cleaner_result.details:
                print_validation_details('cleaner', cleaner_result.details)
                
            success = success and (spectral_result or True) and (cleaner_result or True)
        return success

    def compare_validation_results(self, config: ValidationConfig, result: ValidationResult) -> ValidationResult:
        actual_set = set(result.rules_hit)
        
        if config.should_equal is not None:
            expected_set = set(config.should_equal)
            if expected_set != actual_set:
                result.success = False
                if missing := expected_set - actual_set:
                    result.details.append(f"should hit: {sorted(missing)}")
                if unexpected := actual_set - expected_set:
                    result.details.append(f"should miss: {sorted(unexpected)}")
        
        if config.should_hit is not None:
            required_set = set(config.should_hit)
            if not required_set.issubset(actual_set):
                result.success = False
                if missing := required_set - actual_set:
                    result.details.append(f"should hit: {sorted(missing)}")
        
        if config.should_miss is not None:
            forbidden_set = set(config.should_miss)
            if triggered := (forbidden_set & actual_set):
                result.success = False
                result.details.append(f"should miss: {sorted(triggered)}")
        
        return result
    
