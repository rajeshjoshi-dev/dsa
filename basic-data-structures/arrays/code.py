# Creating Arrays

# 1. Using list
arr_list = [1, 2, 3, 4, 5]

# 2. Using array module
import array

arr = array.array("i", [1, 2, 3, 4, 5])  # 'i' → signed integer

# Basic Operations on Arrays

# 1 Accessing Elements
print(arr[0])  # First element
print(arr[-1])  # Last element

# 2. Traversal
for x in arr:
    print(x, end=" ")
print("")

# 3. Insertion
arr.append(6)  # Add at end
arr.insert(2, 99)  # Insert at index 2

print(arr)

# 4. Deletion
arr.remove(99)  # Remove first occurrence
arr.pop()  # Remove last element
arr.pop(1)  # Remove element at index 1

# 5. Updating
arr[0] = 10  # Update first element

# 6. Searching
print(arr.index(4))  # Find index of first occurrence of 4

# 7. Length
print(len(arr))

# Advanced Operations

# 1. Slicing
print(arr[1:4])  # Elements from index 1 to 3

# 2. Concatenation
arr2 = array.array("i", [7, 8, 9])
arr3 = arr + arr2
print(arr3)

# 3. Reversing
arr.reverse()
print(arr)

# 4. Sorting (convert to list first)
sorted_arr = sorted(arr)
