
from typing import Dict, Any, Union
from ruamel.yaml import YAML
from .core import create_default_pipeline

def clean_specification(
    specification: Union[str, Dict[str, Any]], 
    return_cleaners_hit: bool = False
) -> Union[Dict[str, Any], tuple[Dict[str, Any], list]]:
    """
    Clean an OpenAPI specification.
    
    Args:
        specification: Either a YAML string or a dict containing the specification
        return_cleaners_hit: Whether to return cleaning statistics
        
    Returns:
        If return_cleaners_hit is False: The cleaned specification as a dict
        If return_cleaners_hit is True: A tuple of (cleaned specification, list of cleaner stats)
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
    
    if return_cleaners_hit:
        stats = []
        for cleaner in pipeline.cleaners:
            if cleaner.stats.hit():
                stats.append(cleaner.stats.name)
        return cleaned_spec, stats
    
    return cleaned_spec
