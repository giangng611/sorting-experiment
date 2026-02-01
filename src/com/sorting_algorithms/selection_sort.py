from __future__ import annotations
from typing import List
from base_sorter import BaseSorter
class SelectionSort(BaseSorter):
    """
        Selection Sort algorithm.

        Repeatedly selects the smallest element from the unsorted portion
        and swaps it into its correct position.
        Time complexity: O(n^2) comparisons.
        """