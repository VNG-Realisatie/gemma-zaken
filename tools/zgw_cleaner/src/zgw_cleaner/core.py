from typing import Dict, Any
from dataclasses import dataclass, field
from collections import Counter
from .cleaner import Cleaner
from .cleaners import *
from copy import deepcopy

class CleanupPipeline:
    """Pipeline to run multiple cleaners."""
    def __init__(self):
        self.cleaners = []

    def add_cleaner(self, cleaner: Cleaner):
        self.cleaners.append(cleaner)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        clean_spec = deepcopy(spec)  # Ensure we don't modify the original spec
        for cleaner in self.cleaners:
            clean_spec = cleaner.clean(clean_spec)
        return clean_spec

def create_default_pipeline():
    pipeline = CleanupPipeline()
    pipeline.add_cleaner(RedundantTitleCleaner())
    pipeline.add_cleaner(ComponentHeadersCleaner())
    pipeline.add_cleaner(ComponentPrefixCleaner())
    pipeline.add_cleaner(ResponseConsolidationCleaner())
    pipeline.add_cleaner(CommonResponsesCleaner())
    pipeline.add_cleaner(SchemaMetadataConsolidationCleaner())
    pipeline.add_cleaner(TagsCleaner())
    pipeline.add_cleaner(DescriptionFormatCleaner())
    pipeline.add_cleaner(EnumDescriptionsCleaner())
    pipeline.add_cleaner(DiscriminatorToVariantCleaner())
    pipeline.add_cleaner(StandalonexOfCleaner())
    pipeline.add_cleaner(FieldNameCleaner())
    return pipeline
