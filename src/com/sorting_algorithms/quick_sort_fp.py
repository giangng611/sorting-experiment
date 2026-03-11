from __future__ import annotations
from typing import List
from com.sorting_algorithms.base_sorter import BaseSorter

class QuickSortFirstPivot(BaseSorter):
    """
    Quick Sort using the first element as pivot.

    Average time: O(n log n)
    Worst case: O(n^2)
    """

    def sort(self, arr: List[int]) -> None:
        if arr is None:
            raise ValueError("Input array cannot be None")

        self.reset()
        if len(arr) <= 1:
            return
        self._quick_sort(arr, 0, len(arr) - 1)

    def _quick_sort(self, arr: List[int], first: int, last: int) -> None:
        if first < last:
            split = self._split(arr, first, last)
            self._quick_sort(arr, first, split - 1)
            self._quick_sort(arr, split + 1, last)

    def _split(self, arr: List[int], first: int, last: int) -> int:
        """Partition the array around the first element pivot."""
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