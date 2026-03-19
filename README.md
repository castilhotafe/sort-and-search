

# Sort and Search - Personal Studies

This project contains implementations of common sorting and searching algorithms studied during TAFE sessions 
from  learning materials as well as  personal practice.

---

## Searching Algorithms

### Binary Search
- Works on sorted lists
- Divides the list in half each step
- Time complexity: O(log n)
- Efficient for large datasets

---

## Sorting Algorithms

### Selection Sort
- Finds the smallest element and places it in the correct position
- Repeats for the rest of the list
- Time complexity: O(n^2)
- Simple but inefficient for large lists
- Personal implementation based on the Grokking Algorithms book (O'Reilley)

### Selection Sort (In-place)
- Same logic as selection sort
- Does not create a new list
- Uses swapping instead of removing elements
- More memory efficient
- Personal implementation based on the Grokking Algorithms book (O'Reilley)

### Bubble Sort
- Repeatedly swaps adjacent elements if they are in the wrong order
- Time complexity: O(n^2)
- Very simple but inefficient

### Insertion Sort
- Builds the sorted list one element at a time
- Efficient for small or nearly sorted datasets
- Time complexity: O(n^2), but performs better than bubble and selection sort in practice

### Merge Sort
- Uses divide and conquer
- Splits the list into smaller parts, sorts them, and merges
- Time complexity: O(n log n)
- Requires additional memory

### Quick Sort
- Uses a pivot to partition the list
- Recursively sorts sublists
- Average time complexity: O(n log n)
- Very efficient in practice
- Can be implemented in-place

---

## Key Differences

### Selection Sort vs Merge Sort
- Selection Sort is simple but slow (O(n^2))
- Merge Sort is faster (O(n log n)) but requires extra memory

### Selection Sort vs Quick Sort
- Selection Sort compares all elements repeatedly
- Quick Sort divides the problem using a pivot
- Quick Sort is significantly faster in most cases

---

## Learning Notes

- Selection Sort is useful for understanding sorting fundamentals
- Merge Sort introduces recursion and divide-and-conquer concepts
- Quick Sort is widely used in real-world applications
- In-place algorithms modify the original list instead of creating a new one

---

## Project Structure

- binary_search.py
- selection_sort.py
- selection_sort_inplace.py
- bubble_sort.py
- insertionsort.py
- merge_sort.py
- quick_sort.py
- sorting_bisect.py
- game.py

---

