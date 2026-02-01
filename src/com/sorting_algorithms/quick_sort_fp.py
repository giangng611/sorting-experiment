from __future__ import annotations
from typing import List
from base_sorter import BaseSorter


class QuickSortFirstPivot(BaseSorter):
    """
    Quick Sort using the first element as pivot.

    Average time: O(n log n)
    Worst case: O(n^2)
    """