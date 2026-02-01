from __future__ import annotations
from typing import List
from com.sorting_algorithms.base_sorter import BaseSorter

class MergeSort(BaseSorter):
    """
    Merge Sort algorithm (divide and conquer).

    Recursively splits the array into halves,
    then merges them back in sorted order.
    Time complexity: O(n log n)
    """