from typing import Dict, Any
from dataclasses import dataclass, field
from collections import Counter

@dataclass
class CleanerStats:
    """Statistics for a cleaning operation."""
    name: str
    counts: Counter = field(default_factory=Counter)
    
    def __str__(self):
        if not self.counts:
            return f"{self.name}: no changes made"
        return f"{self.name}: " + ", ".join(f"{k}: {v}" for k, v in self.counts.items())

class Cleaner:
    """Base class for cleanup operations."""
    def __init__(self):
        self.stats = CleanerStats(self.__class__.__name__)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

class CleanupPipeline:
    """Pipeline to run multiple cleaners."""
    def __init__(self):
        self.cleaners = []

    def add_cleaner(self, cleaner: Cleaner):
        self.cleaners.append(cleaner)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        for cleaner in self.cleaners:
            spec = cleaner.clean(spec)
        return spec
