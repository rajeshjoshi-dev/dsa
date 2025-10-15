# Data Structures & Algorithms

- [What are Data Structures?](#what-are-data-structures)
- [Importance of Data Structures](#importance-of-data-structures)
- [Basic Data Structures](#basic-data-structures)

  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Hash Tables](#hash-tables)

- [Algorithmic Complexity](#algorithmic-complexity)

  - [Time vs Space Complexity](#time-vs-space-complexity)
  - [How to Calculate Complexity?](#how-to-calculate-complexity)
  - [Notations](#notations)

- [Sorting Algorithms](#sorting-algorithms)

  - [Bubble Sort](#bubble-sort)
  - [Merge Sort](#merge-sort)
  - [Insertion Sort](#insertion-sort)
  - [Quick Sort](#quick-sort)
  - [Selection Sort](#selection-sort)
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

## Algorithmic Complexity

"Algorithmic Complexity" refers to the computing resources needed by an algorithm to solve a problem. These computing resources can be the time taken for program execution (time complexity), or the space used in memory during its execution (space complexity). The aim is to minimize these resources, so an algorithm that takes less time and space is considered more efficient. Complexity is usually expressed using Big O notation, which describes the upper bound of time or space needs, and explains how they grow in relation to the input size. It's important to analyze and understand the algorithmic complexity to choose or design the most efficient algorithm for a specific use-case.

- Constant
- Logarithmic
- Linear
- Polynomial
- Exponential
- Factorial

### Time vs Space Complexity

### How to Calculate Complexity?

### Notations

- Big O Notation
- Big-θ Notation
- Big-Ω Notation

## Sorting Algorithms

### Bubble Sort

### Merge Sort

### Insertion Sort

### Quick Sort

### Selection Sort

### Heap Sort

## Search Algorithms

## Binary Search

## Linear Search

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
