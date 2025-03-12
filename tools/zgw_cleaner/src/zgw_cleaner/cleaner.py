
from dataclasses import dataclass, field
from typing import Dict, Any
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

