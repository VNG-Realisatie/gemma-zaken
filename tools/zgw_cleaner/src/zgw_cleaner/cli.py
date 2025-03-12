"""Command line interface for ZGW API specification cleanup."""

from pathlib import Path
import configargparse
import sys
import logging

from ruamel.yaml import YAML
from .core import create_default_pipeline

def setup_logging(verbose: bool):
    """Configure logging based on verbosity."""
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format='%(message)s',
        stream=sys.stderr
    )

def create_parser():
    parser = configargparse.ArgumentParser(
        description="Clean up ZGW API specifications",
        default_config_files=['~/.zgw-cleaner.conf', './zgw-cleaner.conf'],
    )
    
    parser.add_argument(
        '-c', '--config',
        is_config_file=True,
        help='Config file path'
    )
    
    parser.add_argument(
        'input_file',
        type=Path,
        help='Input OpenAPI specification file'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Increase output verbosity'
    )

    parser.add_argument(
        '--stats-only', '-s',
        action='store_true',
        help='Only show statistics, do not output cleaned YAML'
    )
    
    return parser

def main():
    """Main entry point for the cleanup tool."""
    parser = create_parser()
    args = parser.parse_args()

    setup_logging(args.verbose)

    if not args.input_file.exists():
        parser.error(f"Input file {args.input_file} does not exist")

    logging.debug(f"Processing {args.input_file}")

    # Initialize YAML
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    # Read YAML
    with open(args.input_file) as f:
        try:
            spec = yaml.load(f)
            if args.verbose:
                print(f"Successfully loaded YAML from {args.input_file}", file=sys.stderr)
        except Exception as e:
            print(f"Error loading YAML: {e}", file=sys.stderr)
            sys.exit(1)

    pipeline = create_default_pipeline()

    # Process
    cleaned_spec = pipeline.clean(spec)

   # Log statistics
    logging.debug("Cleaning statistics:")
    for cleaner in pipeline.cleaners:
        logging.debug(f"  {cleaner.stats}")

    if not args.stats_only:
        yaml.dump(cleaned_spec, sys.stdout)

if __name__ == "__main__":
    main()
