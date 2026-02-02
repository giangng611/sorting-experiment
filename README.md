# Sorting Algorithms Comparison (Python)

This project implements and compares several classic sorting algorithms in Python.  
The goal is to experimentally analyze their performance by counting **data element comparisons** and relating the results to their theoretical time complexity.

---

## Algorithms Implemented

The following sorting algorithms are included:

| Algorithm | Description |
|-----------|-------------|
| Selection Sort | Simple comparison-based sort that repeatedly selects the minimum element |
| Merge Sort | Divide-and-conquer algorithm with stable \(O(n \log n)\) complexity |
| Heap Sort | In-place sort based on binary heap structure |
| Quick Sort (First Pivot) | Quick sort using the first element as pivot |
| Quick Sort (Random Pivot) | Quick sort using a randomly chosen pivot |

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


Results are saved in a CSV file for plotting and analysis.

---

## What Is Being Measured?

We count only **comparisons between array elements** (e.g., `a < b`, `a <= b`, etc.).  
We do **not** count:
- Loop counters
- Index comparisons
- Assignment operations

This allows us to directly compare the *core work* done by each algorithm.

---

## Observed Time Complexity Behavior

Based on the experimental data:

### Selection Sort
- Comparisons grow approximately as **\(n^2\)**
- Nearly identical number of comparisons regardless of input distribution
- Very inefficient for large inputs

### Merge Sort
- Comparisons grow approximately as **\(n \log n\)**
- Very stable performance across different input sizes
- Requires extra memory for merging

### Heap Sort
- Also grows approximately as **\(n \log n\)**
- In-place (no large extra arrays needed)
- Slightly more comparisons than merge sort in practice due to heap operations

### Quick Sort (First Pivot)
- Average-case close to **\(n \log n\)** on random input
- Can degrade toward **\(n^2\)** in bad cases (e.g., nearly sorted input)
- Performance depends heavily on pivot choice

### Quick Sort (Random Pivot)
- Average-case **\(n \log n\)** very consistently
- Avoids worst-case behavior of fixed-pivot quicksort
- Often performs among the best in practice

---

## How to Run

### Run experiment across multiple input sizes:
```bash
python experiment2.py
```
### This generates:
```
results.csv
```

### which can be used for plotting graphs of:

- Comparisons vs Input Size

- Algorithm growth trends