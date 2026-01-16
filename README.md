# Data Structures & Algorithms

- [What are Data Structures?](#what-are-data-structures)
- [Importance of Data Structures](#importance-of-data-structures)
- [Basic Data Structures](#basic-data-structures)

  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Hash Tables](#hash-tables)

- [Algorithmic Complexities](#algorithmic-complexities)

  - [Why Algorithmic Complexity Matters](#why-algorithmic-complexity-matters)
  - [Big-O Notation](#big-o-notation)
  - [Time Complexity](#time-complexity)
  - [Space Complexity](#space-complexity)
  - [Best, Average, and Worst Case](#best-average-and-worst-case)
  - [Dropping Constants and Lower-Order Terms](#dropping-constants-and-lower-order-terms)
  - [Common Pitfalls](#common-pitfalls)
  - [Practical Complexity Comparison](#practical-complexity-comparison)
  - [Algorithmic Complexities Key Takeaways](#algorithmic-complexities-key-takeaways)

- [Sorting Algorithms](#sorting-algorithms)

  - [Bubble Sort](#bubble-sort)
  - [Insertion Sort](#insertion-sort)
  - [Selection Sort](#selection-sort)
  - [Merge Sort](#merge-sort)
  - [Quick Sort](#quick-sort)
  - [Counting Sort](#counting-sort)
  - [Heap Sort](#heap-sort)

- [Search Algorithms](#search-algorithms)

  - [Binary Search](#binary-search)
  - [Linear Search](#linear-search)

- [Tree Data Structures](#tree-data-structures)

  - [Binary Trees](#binary-trees)
  - [Binary Search Trees](#binary-search-trees)
  - [AVL Trees](#avl-trees)
  - [B-Trees](#b-trees)
  - [Heap](#heap)
  - [Tree Traversal](#tree-traversal)

    - [In-Order Traversal](#in-order-traversal)
    - [Out-Order Traversal](#out-order-traversal)
    - [Post-Order Traversal](#post-order-traversal)

  - [Search Algorithms](#tree-search-algorithms)
    - [Breadth First Search](#breadth-first-search)
    - [Depth First Search](#depth-first-search)

- [Graph Data Structure](#graph-data-structure)

  - [Graph Search Algorithms](#graph-search-algorithms)
    - [Breadth First Search](#depth-first-search-1)
    - [Depth First Search](#breadth-first-search-1)
  - [Shortest Path Algorithms](#shortest-path-algorithms)
    - [Dijkstra's Algorithm](#dijkstras-algorithm)
    - [Bellman-Ford Algorithm](#bellman-ford-algorithm)
    - [A\* Algorithm](#a-algorithm)
  - [Minimum Spanning Tree](#minimum-spanning-tree)
    - [Prim's Algorithm](#prims-algorithm)
    - [Kruskal's Algorithm](#kruskals-algorithm)

- [Advanced Data Structures](#advanced-data-structures)

  - [Trie](#trie)
  - [Segment Trees](#segment-trees)
  - [Fenwick Trees](#fenwick-trees)
  - [Disjoint Set (Union-Find)](#disjoint-set-union-find)
  - [Suffix Trees and Arrays](#suffix-trees-and-arrays)

- [Complex Data Structures](#complex-data-structures)

  - [2-3 Trees](#2-3-trees)
  - [B/B+ Trees](#bb-trees)
  - [Skip List](#skip-list)
  - [ISAM](#isam)

- [Indexing](#indexing)

  - [Linear](#linear)
  - [Tree-Based](#tree-based)

- [Problem Solving Techniques](#problem-solving-techniques)

  - [Brute Force](#brute-force)
  - [Backtracking](#backtracking)
  - [Greedy Algorithms](#greedy-algorithms)
  - [Island Traversal](#island-traversal)
  - [Randomised Algorithms](#randomised-algorithms)
  - [Multi-threaded](#multi-threaded)
  - [Divide and Conquer](#divide-and-conquer)
  - [Two Heaps](#two-heaps)
  - [Kth Element](#kth-element)
  - [Recursion](#recursion)
  - [Merge Intervals](#merge-intervals)
  - [Dynamic Programming](#dynamic-programming)
  - [Cyclic Sort](#cyclic-sort)
  - [Two Pointer Technique](#two-pointer-technique)
  - [Fast and Slow Pointers](#fast-and-slow-pointers)
  - [Sliding Window Technique](#sliding-window-technique)

## What are Data Structures?

Data structures are specialized formats for organizing and storing data in a computer so that it can be used efficiently. They provide a means to manage large amounts of data efficiently for uses such as large databases and internet indexing services. They are critical to programming and are used in almost all software systems including web development, operating systems, image editing, and much more. Some common types of data structures are arrays, linked lists, queues, stacks, trees, and graphs. The choice of the data structure often begins from the choice of an abstract data type, a broad type encapsulating various possible data structures."

## Importance of Data Structures

Data structures are crucial in the field of computer science and coding because they offer a method of organizing and storing data in an efficient and manageable format. They're critical because they form the foundation for modern algorithm design. Your ability to choose or design the most suited data structure for a particular task can be the difference between a solution that's functional and efficient and one that isn't. They allow data to be processed in a variety of ways - stored, sorted, ordered, or accessed - which is integral to software or database development. By implementing effective data structures, programmers can enhance performance, ease coding procedures, allow flexibility of data and most importantly, reduce complexity of code in a significant manner.

## Basic Data Structures

The five main types of basic data structures are: Arrays, Linked Lists, Stacks, Queues, and Hash Tables.

- **Arrays** are static data structures that store elements of the same type in contiguous memory locations.
- **Linked Lists** are dynamic data structures that store elements in individual nodes, with each node pointing to the next.
- **Stacks** follow the Last-In-First-Out principle (LIFO) and primarily assist in function calls in most programming languages.
- **Queues** operate on the First-In-First-Out principle (FIFO) and are commonly used in task scheduling.
- **Hash Tables** store key-value pairs allowing for fast insertion, deletion, and search operations.

### Arrays

In Python, the most common structure similar to arrays is the list, but Python also provides a special array module (`array` class) for more memory-efficient storage of homogeneous data (all elements of the same type).

**List**: Can store mixed data types.

**array.array**: Stores only one type of data (e.g., all integers or all floats).

#### When to Use Arrays vs Lists

- Use list if you need flexibility with mixed data types.
- Use array.array if you need memory efficiency and all elements are the same type.
- Use NumPy arrays (`numpy.array`) if you work with numerical data and need high-performance operations (matrix/vector calculations).

#### Summary of Operations

- **Creation**: list, array module, NumPy
- **Accessing**: index, slicing
- **Modification**: update, append, insert
- **Deletion**: remove, pop
- **Searching**: index, in operator
- **Traversal**: loops
- **Other**: length, reverse, concatenation, sorting

#### [Code](./basic-data-structures/arrays/code.py)

### Linked Lists

A linked list is a linear data structure where elements (nodes) are connected using pointers. Each node contains:

- **Data** – value stored.
- **Next** – reference (pointer) to the next node.

Unlike arrays, linked lists do not store data in contiguous memory.

#### Types of Linked Lists

- **Singly Linked List** – Each node points to the next node.
- **Doubly Linked List** – Each node points to both next and previous nodes.
- **Circular Linked List** – Last node points back to the first node.

#### [Code](./basic-data-structures/linked-lists/code.py)

#### [Questions](./basic-data-structures/linked-lists/questions/)

- Calculate the sum of all node values [(sum-of-values)](./basic-data-structures/linked-lists/questions/sum-of-values)
- Find a node with given data [(find-a-node)](./basic-data-structures/linked-lists/questions/find-a-node)
- Reverse a Linked-list [(reverse-linked-list)](./basic-data-structures/linked-lists/questions/reverse-linked-list)
- Zip 2 Linked-lists [(zipper)](./basic-data-structures/linked-lists/questions/zipper)

### Stacks

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.

- The last element added is the first one to be removed.
- Think of it as a pile of plates: you put one plate on top, and you also take the top plate out first.

#### Core Operations of a Stack

A stack supports the following main operations:

- **push(x)** → Add an element x to the top of the stack.
- **pop()** → Remove and return the top element.
- **peek() / top()** → View the top element without removing it.
- **is_empty()** → Check if the stack is empty.
- **size()** → Return the number of elements in the stack.

#### Stack Applications

Stacks are widely used in:

- Undo/Redo in text editors.
- Backtracking in algorithms (e.g., maze solving).
- Function call stack in programming languages.
- Expression evaluation (postfix, prefix).
- Balanced parentheses checking.

#### [Code](./basic-data-structures/stacks/code.py)

#### [Questions](./basic-data-structures/stacks/questions/)

- Balanced Parentheses [(balanced-parentheses)](./basic-data-structures/stacks/questions/balanced-parentheses)

### Queues

A queue is a linear data structure that follows the FIFO (First In, First Out) principle.

- The first element added is the first one to be removed.
- Think of it like people standing in a line: the first person enters first and leaves first.

#### Core Operations of a Queue

A queue supports the following main operations:

- **enqueue(x)** → Add element x to the back (rear) of the queue.
- **dequeue()** → Remove and return the front element.
- **peek() / front()** → View the front element without removing it.
- **is_empty()** → Check if the queue is empty.
- **size()** → Return the number of elements in the queue.

#### Types of Queues

- Simple Queue (FIFO) – as explained above.
- Circular Queue – uses array in circular fashion to optimize space.
- Double-Ended Queue (Deque) – insertion/removal from both ends.
- Priority Queue – elements are removed based on priority, not order.

#### Queue Applications

- CPU scheduling (round-robin, FCFS).
- Task scheduling in operating systems.
- Printer queue.
- Breadth-first search (BFS) in graphs.
- Data buffering (IO operations, streaming).

#### [Code](./basic-data-structures/queues/code.py)

### Hash Tables

A Hash Table (or Hash Map) is a key–value data structure that allows very fast data lookup, insertion, and deletion — typically O(1) on average. It uses a hash function to convert a given key into an index (hash code) where the value is stored in memory.

#### How Hash Tables Work?

1. The key is passed through a hash function (e.g., converting a string to a number).
2. The hash function returns an index in an array (called a bucket).
3. The key–value pair is stored at that index.

If two keys produce the same index (called a collision), we use a collision resolution technique (see below).

#### Core Operations

- **Insert / put(key, value)** – Add or update a key–value pair.
- **Get(key)** – Retrieve the value associated with a key.
- **Delete(key)** – Remove a key–value pair.
- **Contains(key)** – Check if the key exists.
- **Size()** – Get the number of key–value pairs.

#### Collision Resolution Techniques

When two keys hash to the same index, we must handle the collision.
Common techniques include:

1. Chaining (Separate Chaining)

   - Each bucket is a list (linked list or array) of key–value pairs.
   - Example: Python dictionaries use chaining.

2. Open Addressing
   - If one index is full, look for another slot using:
     - Linear probing (next available index)
     - Quadratic probing
     - Double hashing

#### Time & Space Complexity

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Insert    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

#### Applications of Hash Tables

- Counting frequency (e.g., word count, character count).
- Caching (LRU cache, memoization).
- Storing configurations or user sessions.
- Checking duplicates in an array.
- Implementing sets and maps.

#### [Code](./basic-data-structures/hash-tables/code.py)

#### [Questions](./basic-data-structures/hash-tables/questions/)

- Count Word Frequency [(count-word-frequency)](./basic-data-structures/hash-tables/questions/count-word-frequency)

- First Non-Repeating Character [(first-non-repeating-character)](./basic-data-structures/hash-tables/questions/first-non-repeating-character)

## Algorithmic Complexities

Algorithmic complexity describes **how an algorithm’s performance scales** as the size of its input grows. Instead of measuring execution time in seconds (which depends on hardware), we analyze **growth rates**.

### Why Algorithmic Complexity Matters

- Predicts performance on large inputs
- Helps compare algorithms objectively
- Essential for scalability and system design
- Frequently tested in technical interviews

Example problem:

> Sorting 10 items vs sorting 10 million items
> A poorly chosen algorithm can make the difference between milliseconds and hours.

### Big-O Notation

Big-O notation expresses the **upper bound** (worst-case growth) of an algorithm.
Following are some common Complexity Classes (from best to worst).

| Big-O      | Name         | Example            |
| ---------- | ------------ | ------------------ |
| O(1)       | Constant     | Array access       |
| O(log n)   | Logarithmic  | Binary search      |
| O(n)       | Linear       | Loop through array |
| O(n log n) | Linearithmic | Merge sort         |
| O(n²)      | Quadratic    | Nested loops       |
| O(2ⁿ)      | Exponential  | Recursive subsets  |
| O(n!)      | Factorial    | Permutations       |

### Time Complexity

#### [O(1) — Constant Time](./algorithmic-complexities/time-complexity/constant-time/code.py)

Execution time **does not depend on input size**.

- Always one operation
- Best possible complexity

#### [O(n) — Linear Time](./algorithmic-complexities/time-complexity/linear-time/code.py)

Time grows **proportionally** with input size.

If `n` doubles → time doubles.

#### [O(n²) — Quadratic Time](./algorithmic-complexities/time-complexity/quadratic-time/code.py)

Common with **nested loops**.

- If `n = 1,000` → 1,000,000 operations
- Becomes slow very quickly

#### [O(log n) — Logarithmic Time](./algorithmic-complexities/time-complexity/logarithmic-time/code.py)

Problem size **halves each step**.

- Very efficient
- Requires sorted input

#### [O(n log n) — Linearithmic Time](./algorithmic-complexities/time-complexity/linearithmic-time/code.py)

Common in **efficient sorting algorithms**.

- Best practical performance for comparison-based sorting

#### [O(2ⁿ) — Exponential Time](./algorithmic-complexities/time-complexity/exponential-time/code.py)

Typically appears in **brute-force recursion**.

- Very inefficient
- Small increases in `n` cause massive slowdowns

### Space Complexity

Space complexity measures **extra memory used**, excluding input.

#### [O(1) Space — In Place](./algorithmic-complexities/space-complexity/in-place/code.py)

- Uses a constant number of variables

#### [O(n) Space](./algorithmic-complexities/space-complexity/o-n-space/code.py)

- Extra memory proportional to input size

### Best, Average, and Worst Case

Example: Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

| Case    | Scenario          | Complexity |
| ------- | ----------------- | ---------- |
| Best    | Target at index 0 | O(1)       |
| Average | Random position   | O(n)       |
| Worst   | Not present       | O(n)       |

### Dropping Constants and Lower-Order Terms

Big-O ignores constants:

```text
O(3n + 10) → O(n)
O(n² + n) → O(n²)
```

Reason:

- Growth rate matters more than exact count

### Common Pitfalls

❌ Mistaking multiple loops for O(n²)

```python
for i in arr:
    print(i)

for j in arr:
    print(j)
```

✅ This is **O(n)**, not O(n²)

❌ Ignoring hidden loops (e.g., `.in`, `.count()`)

```python
if x in arr:  # O(n)
    print("Found")
```

### Practical Complexity Comparison

| n         | O(n)   | O(n log n) | O(n²)       |
| --------- | ------ | ---------- | ----------- |
| 100       | 100    | ~664       | 10,000      |
| 10,000    | 10,000 | ~132,877   | 100,000,000 |
| 1,000,000 | 1M     | ~20M       | 1T          |

### Algorithmic Complexities Key Takeaways

- Big-O measures **growth**, not exact time
- Nested loops usually → **quadratic**
- Recursion affects **space complexity**
- Prefer **O(log n)** and **O(n log n)** when possible
- Always think about **scalability**

## Sorting Algorithms

### Bubble Sort

Bubble sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares each pair of adjacent elements, and swaps them if they are in the wrong order. With each pass, the largest remaining element “bubbles up” to its correct position at the end.

**Key points:**

- Works by repeatedly swapping adjacent out-of-order elements
- After each full pass, one more element is in its final position
- Worst-case and average time complexity: **O(n²)**
- Space complexity: **O(1)** (in-place)
- Easy to understand but inefficient for large datasets

#### [Code](./sorting-algorithms/bubble-sort/code.py)

### Insertion Sort

Insertion sort builds the final sorted list one element at a time. It takes each element and “inserts” it into its correct position among the elements already sorted on its left.

**Key points:**

- Works like sorting playing cards in your hand
- For each element, shift larger elements to the right to make space
- Efficient for small or nearly sorted datasets
- Worst-case and average time complexity: **O(n²)**
- Best case (already sorted): **O(n)**
- Space complexity: **O(1)** (in-place)

#### [Code](./sorting-algorithms/insertion-sort/code.py)

### Selection Sort

Selection sort repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of that unsorted portion. After each pass, the boundary between the sorted and unsorted sections moves by one.

**Key points:**

- Finds the minimum element and places it in its correct position
- Performs **(n-1)** passes regardless of input order
- Time complexity (best, average, worst): **O(n²)**
- Space complexity: **O(1)** (in-place)
- Simple to implement but inefficient for large datasets

#### [Code](./sorting-algorithms/selection-sort/code.py)

### Merge Sort

Merge sort is a divide-and-conquer sorting algorithm. It works by recursively splitting the list into two halves, sorting each half, and then _merging_ the two sorted halves into one sorted list.

**Key points:**

- Uses “divide → sort → merge” strategy
- Very efficient for large datasets
- Time complexity (best, average, worst): **O(n log n)**
- Space complexity: **O(n)** due to extra arrays used for merging
- Stable sorting algorithm (preserves order of equal elements)

#### [Code](./sorting-algorithms/merge-sort/code.py)

### Quick Sort

Quick sort is a fast, divide-and-conquer sorting algorithm. It works by choosing a _pivot_ element, partitioning the list so that elements smaller than the pivot go to one side and larger elements go to the other, and then recursively sorting the two partitions.

**Key points:**

- Uses “partition → recursively sort” strategy
- Very efficient in practice
- Average time complexity: **O(n log n)**
- Worst-case time complexity: **O(n²)** (usually avoided with good pivot choices)
- Space complexity: **O(log n)** on average (due to recursion)
- Not stable by default, but very widely used due to speed and simplicity

#### [Code](./sorting-algorithms/quick-sort/code.py)

### Counting Sort

Counting sort is a non-comparison sorting algorithm used when the range of input values is known and not too large. It counts how many times each value appears, then uses these counts to place elements directly into their correct positions in the output array.

**Key points:**

- Works by counting occurrences of each value
- Efficient when the range of numbers (**k**) is small relative to the number of items (**n**)
- Time complexity: **O(n + k)**
- Space complexity: **O(k)**
- Stable when implemented carefully
- Not suitable for sorting data with very large value ranges relative to the input size

#### [Code](./sorting-algorithms/counting-sort/code.py)

### Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a **binary heap** data structure. It first builds a max-heap from the input, then repeatedly removes the largest element (the root of the heap) and places it at the end of the array, shrinking the heap each time.

**Key points:**

- Uses a max-heap to repeatedly extract the largest element
- In-place sorting (requires no extra significant memory)
- Time complexity (best, average, worst): **O(n log n)**
- Space complexity: **O(1)**
- Not stable, but reliable and efficient for large datasets

#### [Code](./sorting-algorithms/heap-sort/code.py)

Resources

- https://youtu.be/gcRUIO-8r3U

## Search Algorithms

### Binary Search

### Linear Search

## Tree Data Structures

### Binary Trees

### Binary Search Trees

### AVL Trees

### B-Trees

### Heap

### Tree Traversal

#### In-Order Traversal

#### Out-Order Traversal

#### Post-Order Traversal

### Tree Search Algorithms

#### Breadth First Search

#### Depth First Search

## Graph Data Structure

### Graph Search Algorithms

#### Breadth First Search

#### Depth First Search

### Shortest Path Algorithms

#### Dijkstra's Algorithm

#### Bellman-Ford Algorithm

#### A\* Algorithm

### Minimum Spanning Tree

#### Prim's Algorithm

#### Kruskal's Algorithm

## Advanced Data Structures

### Trie

### Segment Trees

### Fenwick Trees

### Disjoint Set (Union-Find)

### Suffix Trees and Arrays

## Complex Data Structures

### 2-3 Trees

### B/B+ Trees

### Skip List

### ISAM

## Indexing

### Linear

### Tree-Based

## Problem Solving Techniques

### Brute Force

### Backtracking

### Greedy Algorithms

### Island Traversal

### Randomised Algorithms

### Multi-threaded

### Divide and Conquer

### Two Heaps

### Kth Element

### Recursion

### Merge Intervals

### Dynamic Programming

### Cyclic Sort

### Two Pointer Technique

### Fast and Slow Pointers

### Sliding Window Technique
