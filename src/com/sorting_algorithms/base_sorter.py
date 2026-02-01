from __future__ import annotations
from typing import List
class BaseSorter:
    """
        Base class that provides comparison counting utilities.
        We count ONLY comparisons between data elements (e.g., a < b, a <= b, a > b).
        """

    def __init__(self) -> None:
        # Total number of comparisons
        self._comparisons: int = 0

    def reset(self) -> None:
        # Reset the comparison counter before each sort
        self._comparisons = 0;

    def comparisons(self) -> int:
        # Return the number of comparisons performed
        return self._comparisons;

    # ---- Comparison helper method ----
    # Each of these increments the counter once and performs the comparison.

    def lt (self, a: int, b: int) -> bool:
        # Return true if a < b, counting one comparison
        self._comparisons += 1;
        return a < b

    def gt (self, a: int, b: int) -> bool:
        # Return true if a > b, counting one comparison
        self._comparisons += 1;
        return a > b

    def le (self, a: int, b: int) -> bool:
        # Return true if a <= b, counting one comparison
        self._comparisons += 1;
        return a <= b

    def ge(self, a: int, b: int) -> bool:
        # Return true if a >= b, counting one comparison
        self._comparisons += 1;
        return a >= b

    def sort(self, arr: List[int]) -> None:
        # Subclasses must implement this method
        raise NotImplementedError("Subclasses must implement sort(arr)")