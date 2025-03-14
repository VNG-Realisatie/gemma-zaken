import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from ruamel.yaml import YAML
import json
from ..validator import ValidationResult, ValidationConfig

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
                    actual_codes = sorted(set(v['code'] for v in violations))
                    return ValidationResult(
                        rules_hit=actual_codes,
                        success=True  # Base success, will be evaluated against config later
                    )

                return []

            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Spectral execution failed: {e.stderr}")
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse Spectral output: {e}")

