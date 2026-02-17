from __future__ import annotations
from typing import List
from com.sorting_algorithms.base_sorter import BaseSorter

class HeapSort(BaseSorter):
    """
    Heap Sort algorithm.

    Builds a max heap, then repeatedly removes the largest element.
    Time complexity: O(n log n)
    """

    def sort(self, arr: List[int]) -> None:
        if arr is None:
            raise ValueError("Input array cannot be None")

        self.reset()
        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self._reheap_down(arr, i, n - 1)

        # Extract elements one by one
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._reheap_down(arr, 0, end - 1)

    def _reheap_down(self, arr: List[int], root: int, bottom: int) -> None:
        """Ensure heap property for subtree rooted at index root."""
        left = root * 2 + 1
        right = root * 2 + 2

        if left <= bottom:
            if left == bottom:
                max_child = left
            else:
                if self.le(arr[left], arr[right]):
                    max_child = right
                else:
                    max_child = left

            if self.lt(arr[root], arr[max_child]):
                arr[root], arr[max_child] = arr[max_child], arr[root]
                self._reheap_down(arr, max_child, bottom)