
from typing import Dict, Any
from collections import Counter

class CleanerStats:
    """Statistics for a cleaning operation."""
    def __init__(self, name: str):
        self.name = name
        self.counts = Counter()

    def __str__(self):
        if not self.counts:
            return f"{self.name}: no changes made"
        return f"{self.name}: " + ", ".join(f"{k}: {v}" for k, v in self.counts.items())

    def hit(self):
        return self.counts
    
    def miss(self):
        return not self.counts

class Cleaner:
    """Base class for cleanup operations."""
    def __init__(self, cleaner_name=None):
        if cleaner_name is None:
            cleaner_name = self.__class__.__name__
        self.stats = CleanerStats(cleaner_name)

    def clean(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

