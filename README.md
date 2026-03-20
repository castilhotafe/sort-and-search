
# Sort and Search - Personal Studies

This project contains implementations of common sorting and searching algorithms studied during TAFE sessions
from learning materials as well as personal practice. The codebase is organized into distinct modules covering
algorithms, performance testing, and Python's magic operators.

---

## Project Structure

```
sort_and_search-personal_studies/
├── searching_algorithms/     # Search algorithm implementations
├── sorting_algorithms/        # Sorting algorithm implementations
└── magic_operators/          # Python magic methods and operator overloading
```

---

## Searching Algorithms

Located in `searching_algorithms/`

### Binary Search (`binary_search.py`)
- Works on sorted lists
- Divides the list in half each step
- Time complexity: O(log n)
- Efficient for large datasets

### Linear Search Performance Exercise (`exercise_1.py`)
- Performance benchmarking of linear search
- Generates 10,000 unique random values
- Averages search time over 100 runs
- Demonstrates impact of sorted vs unsorted data on search performance

### Guessing Game (`game.py`)
- Interactive number guessing game using OOP principles
- Implements binary search logic for efficient guessing
- Supports custom prompts and configurable range
- Tracks number of attempts

---

## Sorting Algorithms

Located in `sorting_algorithms/`

### Selection Sort (`selecion_sort.py`)
- Finds the smallest element and places it in the correct position
- Repeats for the rest of the list
- Time complexity: O(n^2)
- Simple but inefficient for large lists
- Implementation based on the Grokking Algorithms book (O'Reilly)

### Selection Sort (In-place) (`selection_sort_inplace.py`)
- Same logic as selection sort
- Does not create a new list
- Uses swapping instead of removing elements
- More memory efficient
- Implementation based on the Grokking Algorithms book (O'Reilly)

### Bubble Sort (`bubblesort.py`)
- Repeatedly swaps adjacent elements if they are in the wrong order
- Time complexity: O(n^2)
- Very simple but inefficient

### Insertion Sort (`insertionsort.py`)
- Builds the sorted list one element at a time
- Efficient for small or nearly sorted datasets
- Time complexity: O(n^2), but performs better than bubble and selection sort in practice

### Merge Sort (`merge_sort.py`)
- Uses divide and conquer strategy
- Splits the list into smaller parts, sorts them, and merges
- Time complexity: O(n log n)
- Requires additional memory

### Quick Sort (`quick_sort.py`)
- Uses a pivot to partition the list
- Recursively sorts sublists
- Average time complexity: O(n log n)
- Very efficient in practice
- Can be implemented in-place

### Bisect Sorting (`sorting_bisect.py`)
- Demonstrates Python's bisect module for maintaining sorted lists
- Efficient for insertion into already sorted lists

---

## Python Magic Operators

Located in `magic_operators/`

### BankAccount Class (`magic_operators.py`)
Demonstrates implementation of Python's magic methods (dunder methods):

- `__init__()` - Object initialization
- `__len__()` - Makes object work with `len()` function
- `__iter__()` - Makes object iterable (for loops, sorted())
- `__gt__()` - Defines greater-than comparison (>)
- `__lt__()` - Defines less-than comparison (<)
- `__eq__()` - Defines equality comparison (==)
- `@property` - Creates managed attributes with getters

**Key Concepts:**
- Container protocol implementation
- Comparison operators for custom sorting
- Encapsulation with internal `_accounts` list
- Returns sorted copies during iteration
- In-place sorting with `sort_accounts_in_place()`

---

## Key Differences

### Selection Sort vs Merge Sort
- Selection Sort is simple but slow (O(n^2))
- Merge Sort is faster (O(n log n)) but requires extra memory

### Selection Sort vs Quick Sort
- Selection Sort compares all elements repeatedly
- Quick Sort divides the problem using a pivot
- Quick Sort is significantly faster in most cases

### Binary Search vs Linear Search
- Binary Search requires sorted data (O(log n))
- Linear Search works on any data (O(n))
- As demonstrated in `exercise_1.py`, performance differences are significant at scale

---

## Learning Notes

- Selection Sort is useful for understanding sorting fundamentals
- Merge Sort introduces recursion and divide-and-conquer concepts
- Quick Sort is widely used in real-world applications
- In-place algorithms modify the original list instead of creating a new one
- Magic operators enable custom objects to work seamlessly with Python's built-in functions
- Performance benchmarking helps understand theoretical vs practical algorithm behavior

---
