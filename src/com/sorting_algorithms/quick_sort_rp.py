from __future__ import annotations
from typing import List, Optional
import random
from com.sorting_algorithms.base_sorter import BaseSorter

class QuickSortRandomPivot(BaseSorter):
    """
    Quick Sort using a random pivot.

    Helps avoid worst-case behavior of fixed pivot selection.
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        super().__init__()
        self._rng = random.Random(seed)

    def sort(self, arr: List[int]) -> None:
        if arr is None:
            raise ValueError("Input array cannot be None")

        self.reset()
        if len(arr) <= 1:
            return
        self._quick_sort(arr, 0, len(arr) - 1)

    def _quick_sort(self, arr: List[int], first: int, last: int) -> None:
        if first < last:
            pivot_idx = self._rng.randint(first, last)
            arr[first], arr[pivot_idx] = arr[pivot_idx], arr[first]

            split = self._split(arr, first, last)
            self._quick_sort(arr, first, split - 1)
            self._quick_sort(arr, split + 1, last)

    def _split(self, arr: List[int], first: int, last: int) -> int:
        split_val = arr[first]
        save_first = first
        first += 1

        while True:
            while first <= last and not self.gt(arr[first], split_val):
                first += 1

            while first <= last and not self.le(arr[last], split_val):
                last -= 1

            if first < last:
                arr[first], arr[last] = arr[last], arr[first]
                first += 1
                last -= 1
            else:
                break

        arr[save_first], arr[last] = arr[last], arr[save_first]
        return last