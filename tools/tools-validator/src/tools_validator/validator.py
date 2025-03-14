
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ValidationResult:
    rules_hit: List[str]
    success: bool
    details: List[str] = field(default_factory=list)

@dataclass
class ValidationConfig:
    should_equal: Optional[List[str]] = None
    should_hit: Optional[List[str]] = None
    should_miss: Optional[List[str]] = None


