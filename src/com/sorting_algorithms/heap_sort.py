from __future__ import annotations
from typing import List
from com.sorting_algorithms.base_sorter import BaseSorter

class HeapSort(BaseSorter):
    """
    Heap Sort algorithm.

    Builds a max heap, then repeatedly removes the largest element.
    Time complexity: O(n log n)
    """