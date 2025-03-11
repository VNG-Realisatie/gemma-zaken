import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from ruamel.yaml import YAML
import json

@dataclass
class SpectralValidationConfig:
    exact_match: Optional[List[str]] = None
    contains: Optional[List[str]] = None
    not_contains: Optional[List[str]] = None

class SpectralValidator:
    def __init__(self, ruleset_path: Optional[Path] = None):
        self.ruleset_path = ruleset_path
        self.yaml = YAML()
        # Configure ruamel.yaml to maintain OpenAPI formatting
        self.yaml.indent(mapping=2, sequence=4, offset=2)
        self.yaml.preserve_quotes = True

    def run_spectral(self, spec: Dict) -> List[str]:
        """
        Validate an OpenAPI spec using Spectral.
        Returns a list of rule IDs that were triggered.
        """
        # Create a temporary file for the spec
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as temp_spec:
            # Write the spec to the temp file as YAML
            self.yaml.dump(spec, temp_spec)
            temp_spec.flush()

            # Build the spectral command
            cmd = ['npx', 'spectral', 'lint', temp_spec.name, '--format', 'json']
            
            # Add ruleset if specified
            if self.ruleset_path:
                cmd.extend(['--ruleset', str(self.ruleset_path)])

            try:
                # Run spectral
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=False  # Don't raise on lint errors
                )

                # Parse the output
                if result.stdout:
                    violations = json.loads(result.stdout)

                    #print(violations)

                    # Extract unique rule IDs from violations
                    return sorted(set(v['code'] for v in violations))
                return []

            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Spectral execution failed: {e.stderr}")
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse Spectral output: {e}")

    def compare_results(self, config: SpectralValidationConfig, actual_codes: List[str]) -> dict:
        """
        Compare actual results against the validation configuration.
        Returns dict with results per mode.
        """
        actual_set = set(actual_codes)
        results = {
            'rules_triggered': sorted(actual_set),
            'modes': {}
        }

        if config.exact_match is not None:
            expected_set = set(config.exact_match)
            mode_result = {'success': expected_set == actual_set, 'details': []}
            if missing := expected_set - actual_set:
                mode_result['details'].append(f"Missing rules: {sorted(missing)}")
            if unexpected := actual_set - expected_set:
                mode_result['details'].append(f"Unexpected rules: {sorted(unexpected)}")
            results['modes']['spectral-exact-match '] = mode_result

        if config.contains is not None:
            required_set = set(config.contains)
            mode_result = {'success': required_set.issubset(actual_set), 'details': []}
            if missing := required_set - actual_set:
                mode_result['details'].append(f"Missing rules: {sorted(missing)}")
            results['modes']['spectral-contains    '] = mode_result

        if config.not_contains is not None:
            forbidden_set = set(config.not_contains)
            triggered = forbidden_set & actual_set
            mode_result = {'success': not triggered, 'details': []}
            if triggered:
                mode_result['details'].append(f"Forbidden rules: {sorted(triggered)}")
            results['modes']['spectral-not-contains'] = mode_result

        return results

    def validate_spec(self, spec: Dict) -> bool:
        validator_info = spec.get('x-tools-validator', {})
        spec_id = validator_info.get('id', 'unknown')
    
        print(f"\nValidating spec: {spec_id}")
    
        if not (spectral_config := validator_info.get('spectral')):
            print("  No spectral configuration specified - skipping")
            return True

        config = SpectralValidationConfig(
            exact_match=spectral_config.get('exact_match'),
            contains=spectral_config.get('contains'),
            not_contains=spectral_config.get('not_contains')
        )

        actual_codes = self.run_spectral(spec)
        results = self.compare_results(config, actual_codes)
    
        # Print rules triggered
        #print(f"  Rules triggered: {results['rules_triggered']}")
    
        # Print results for each mode
        success = True
        for mode, result in results['modes'].items():
            print(f"  {mode}: {'✓ PASS' if result['success'] else '✗ FAIL'}")
            if not result['success'] and result['details']:
                for detail in result['details']:
                    print(f"    {detail}")
            success = success and result['success']
    
        return success
