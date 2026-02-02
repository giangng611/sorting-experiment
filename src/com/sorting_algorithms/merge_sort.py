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

    def sort(self, arr: List[int]) -> None:
        if arr is None:
            raise ValueError("Input array is None")

        self.reset()

        if len(arr) < 2:
            return

        self._merge_sort(arr, 0, len(arr) - 1)

    def _merge_sort(self, arr: List[int], first: int, last: int) -> None:
        # Recursively sort subarray[first:last]
        if first < last:
            mid = (last + first) // 2
            self._merge_sort(arr, first, mid)
            self._merge_sort(arr, mid + 1, last)
            self._merge(arr, first, mid, mid + 1, last)

    def _merge(self, arr: List[int], left_first: int, left_last: int, right_first: int, right_last: int) -> None:
        """
        Merge two sorted arrays.
        :param arr:
        :param left_first:
        :param left_last:
        :param right_first:
        :param right_last:
        :return:
        """
        temp = [0] * len(arr)
        idx = left_first
        save_first = left_first

        # Merge while both halves have elements
        while left_first <= left_last and right_first <= right_last:
            if self.lt(arr[left_first], arr[right_first]):
                temp[idx] = arr[left_first]
                left_first += 1
            else:
                temp[idx] = arr[right_first]
                right_first += 1
            idx += 1

        # Copy remaining elements
        while left_first <= left_last:
            temp[idx] = arr[left_first]
            left_first += 1
            idx += 1

        while right_first <= right_last:
            temp[idx] = arr[right_first]
            right_first += 1
            idx += 1

        for i in range(save_first, right_last + 1):
            arr[i] = temp[i]




