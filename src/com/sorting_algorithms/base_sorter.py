from __future__ import annotations
from typing import List
class BaseSorter:
    """
        Base class that provides comparison counting utilities.
        We count ONLY comparisons between data elements (e.g., a < b, a <= b, a > b).
        """