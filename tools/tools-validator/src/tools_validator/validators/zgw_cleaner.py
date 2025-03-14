from dataclasses import dataclass
from typing import Dict, Optional
from ruamel.yaml import YAML
from zgw_cleaner.api import clean_specification
from ..validator import ValidationResult

@dataclass
class ZgwCleanerValidationConfig:
    target_id: Optional[str] = None

class ZgwCleanerValidator:
    def __init__(self):
        self.yaml = YAML()

    def clean(self, spec: Dict) -> Dict:
        """
        Clean the specification using the zgw_cleaner API.
        
        Args:
            spec: Dictionary containing the OpenAPI specification
            
        Returns:
            Dict: The cleaned specification
        """
        cleaned_spec, cleaners_hit = clean_specification(spec, return_cleaners_hit=True)
        actual_codes = sorted(cleaners_hit)
        result = ValidationResult(
            rules_hit=actual_codes,
            success=True  # Base success, will be evaluated against config later
        )
        return cleaned_spec, result

    def compare_specs(self, cleaned_spec: Dict, target_spec: Dict) -> bool:
        """
        Compare cleaned spec with target spec.
        Returns True if they match.
        
        Args:
            cleaned_spec: The cleaned specification
            target_spec: The target specification to compare against
            
        Returns:
            bool: True if specifications match
        """
        # Filter out x-tools-validator from both specs
        filtered_dict1 = {k: v for k, v in cleaned_spec.items() if k != 'x-tools-validator'}
        filtered_dict2 = {k: v for k, v in target_spec.items() if k != 'x-tools-validator'}
        return filtered_dict1 == filtered_dict2
