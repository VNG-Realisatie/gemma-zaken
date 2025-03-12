
from typing import Dict, Any, Union
from ruamel.yaml import YAML
from .core import create_default_pipeline

def clean_specification(
    specification: Union[str, Dict[str, Any]], 
    return_stats: bool = False
) -> Union[Dict[str, Any], tuple[Dict[str, Any], list]]:
    """
    Clean an OpenAPI specification.
    
    Args:
        specification: Either a YAML string or a dict containing the specification
        return_stats: Whether to return cleaning statistics
        
    Returns:
        If return_stats is False: The cleaned specification as a dict
        If return_stats is True: A tuple of (cleaned specification, list of cleaner stats)
    """
    yaml = YAML()
    yaml.preserve_quotes = True
    
    # Parse YAML if string input
    if isinstance(specification, str):
        spec = yaml.load(specification)
    else:
        spec = specification

    # Setup and run pipeline
    pipeline = create_default_pipeline()

    cleaned_spec = pipeline.clean(spec)
    
    if return_stats:
        stats = [cleaner.stats for cleaner in pipeline.cleaners]
        return cleaned_spec, stats
    
    return cleaned_spec
