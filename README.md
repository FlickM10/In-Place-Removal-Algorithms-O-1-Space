# In-Place Removal Algorithms – O(1) Space Classics

Constant-space solutions for removing elements from arrays and singly-linked lists.

All implementations modify the input in-place and use only a constant amount of extra memory.

### Array-based (Sorted & Unsorted)

| File                                 | Problem Type                                  | Key Idea                                    | Time   | Space |
|--------------------------------------|-----------------------------------------------|---------------------------------------------|--------|-------|
| `remove_duplicates_26.py`            | Sorted array – keep at most 1 occurrence      | Two-pointer: compare with previous          | O(n)   | O(1)  |
| `remove_element_27.py`               | Unsorted array – remove all instances of val  | Two-pointer: compare with target value      | O(n)   | O(1)  |
| `remove_duplicates_twice_80.py`      | Sorted array – keep at most 2 occurrences     | Two-pointer: compare with element at k-2    | O(n)   | O(1)  |

### Linked List-based

| File                                      | Problem Type                                           | Key Idea                                          | Time   | Space |
|-------------------------------------------|--------------------------------------------------------|---------------------------------------------------|--------|-------|
| `remove_duplicates_linkedlist_83.py`      | Sorted list – keep exactly 1 occurrence                | Single pointer + bypass duplicates                | O(n)   | O(1)  |
| `remove_linkedlist_val_203.py`            | Any list – remove all nodes equal to val               | Dummy node + prev pointer                         | O(n)   | O(1)  |
| `remove_duplicates_linkedlist_all_82.py`  | Sorted list – delete entire duplicate groups (keep none) | Dummy + prev + inner skip loop                  | O(n)   | O(1)  |

### Advantages of the Two-Pointer / Dummy-Prev Approach

- Optimal O(1) extra space in all cases
- Single pass through the data structure
- No recursion → no stack overflow risk
- Preserves relative order of kept elements
- Generalizes easily to “keep at most k occurrences” variations

These patterns form the foundation of constant-space modification problems in technical interviews and production systems.
