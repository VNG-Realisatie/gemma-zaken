import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional
from ruamel.yaml import YAML
from zgw_cleaner.cli import main as zgw_cleaner_main

@dataclass
class ZgwCleanerValidationConfig:
    target_id: Optional[str] = None
       
class ZgwCleanerValidator:
    def __init__(self, cleaner_path: str = "zgw-cleaner"):
        self.cleaner_path = cleaner_path
        self.yaml = YAML()

    def clean(self, spec: Dict) -> Dict:
        """
        Run the cleaner on the spec and return the cleaned version.
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as temp_file:
            # Write the spec to temp file
            self.yaml.dump(spec, temp_file)
            temp_file.flush()

            # Run cleaner
            try:
                result = subprocess.run(
                    [self.cleaner_path, temp_file.name],
                    capture_output=True,
                    text=True,
                    check=True
                )
                # Parse the cleaned output
                cleaned_spec = self.yaml.load(result.stdout)
                return cleaned_spec
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Cleaner execution failed: {e.stderr}")

    def compare_specs(self, cleaned_spec: Dict, target_spec: Dict) -> bool:
        """
        Compare cleaned spec with target spec.
        Returns True if they match.
        """
        # TODO: Implement proper comparison logic
        # This is a simple equality check for now
        return cleaned_spec == target_spec

