from __future__ import annotations
import csv
import os
import random
from typing import List, Tuple

from com.sorting_algorithms.selection_sort import SelectionSort
from com.sorting_algorithms.merge_sort import MergeSort
from com.sorting_algorithms.heap_sort import HeapSort
from com.sorting_algorithms.quick_sort_fp import QuickSortFirstPivot
from com.sorting_algorithms.quick_sort_rp import QuickSortRandomPivot

def generate_random_array(n: int, seed: int) -> List[int]:
    # Generate a list of integers
    rng = random.Random(seed)

    arr = []
    for i in range(n):
        arr.append(rng.randrange(n * 10))
    return arr

def main() -> None:
    """
    Run exxperiment:
    Measure how comparison counts grow with input size
    """
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
    base_seed = 2026

    sorters: List[Tuple[str, object]] = [
        ("Selection Sort", SelectionSort()),
        ("Merge Sort", MergeSort()),
    ]

    rows = [("n", "algorithm", "comparisons")]

    for n in sizes:
        base = generate_random_array(n, seed=base_seed + n)

        for name, sorter in sorters:
            arr = base[:]
            sorter.sort(arr)
            rows.append((n, name, sorter.comparisons()))
            print(f"n={n:<6} algo={name:<9} comparisons={sorter.comparisons()}")

    os.makedirs("../../results", exist_ok=True)

    with open("../../results/results.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

    print("\nResults saved to results/results.csv")

if __name__ == "__main__":
    main()








