from __future__ import annotations
from typing import List
from com.sorting_algorithms.base_sorter import BaseSorter
class SelectionSort(BaseSorter):
    """
        Selection Sort algorithm.

        Repeatedly selects the smallest element from the unsorted portion
        and swaps it into its correct position.
        Time complexity: O(n^2) comparisons.
        """
    def sort(self, arr: List[int]) -> None:
        if arr is None:
            raise ValueError("arr cannot be None")

        # Reset comparison counter
        self.reset()

        n = len(arr)

        for i in range(n - 1):
            min_index = i

            # Find index of minimum element
            for j in range(i + 1, n):
                if self.lt(arr[j], arr[min_index]):
                    min_index = j

            # Swap current position with found minimum
            arr[i], arr[min_index] = arr[min_index], arr[i]
