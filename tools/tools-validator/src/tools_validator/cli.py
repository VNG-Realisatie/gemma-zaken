#!/usr/bin/env python3
import sys
from pathlib import Path
import configargparse
from .core import ToolsValidator

def parse_args():
    parser = configargparse.ArgumentParser(
        description="Validate OpenAPI specs against tools and expected results"
    )
    parser.add_argument(
        "--test-cases-dir",
        required=True,
        type=Path,
        help="Directory containing YAML files with OpenAPI test cases",
    )
    parser.add_argument(
        "--spectral-ruleset",
        type=Path,
        help="Path to Spectral ruleset file",
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    if not args.test_cases_dir.is_dir():
        print(f"Error: {args.test_cases_dir} is not a directory")
        sys.exit(1)
        
    validator = ToolsValidator(
        test_cases_dir=args.test_cases_dir,
        spectral_ruleset=args.spectral_ruleset
    )
    
    success = validator.validate_all()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
