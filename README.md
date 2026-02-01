# Sorting Algorithms Comparison (Python)

This project implements and compares several classic sorting algorithms in Python.  
The goal is to experimentally analyze their performance by counting **data element comparisons** and relating the results to their theoretical time complexity.

---

## Algorithms Implemented

The following sorting algorithms are included:

| Code | Algorithm | Description |
|------|-----------|-------------|
| `s` | Selection Sort | Simple comparison-based sort that repeatedly selects the minimum element |
| `m` | Merge Sort | Divide-and-conquer algorithm with stable \(O(n \log n)\) complexity |
| `h` | Heap Sort | In-place sort based on binary heap structure |
| `q` | Quick Sort (First Pivot) | Quick sort using the first element as pivot |
| `r` | Quick Sort (Random Pivot) | Quick sort using a randomly chosen pivot |

---

## Experiment Design

This project runs **one main experiment**:

> Measure how the number of **data comparisons** grows as input size increases.

### Procedure
For each input size \(n\):

1. Generate a random integer array of size \(n\)
2. Make identical copies of the array
3. Sort each copy using a different algorithm
4. Record the number of **comparisons between data elements only**

Example input sizes:
100, 200, 500, 1000, 2000, 5000, 10000

