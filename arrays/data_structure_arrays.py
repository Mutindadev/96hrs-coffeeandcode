# In Python, lists are used as arrays.
# The index of an array starts from 0.
# Example:
# index: 0  1   2   3   4
# array: [5, 10, 15, 20, 25]

# To access an element in the array, we use square brackets with the index.
# For example, to access the element at index 2, we would write:
# array[2]

# Define a list (which serves as an array in Python)
arr = [10, 20, 30, 40, 50]

# Access an element
print(arr[2])

# Update an element
arr[2] = 55
print(arr[2])

# Insert an element at the end of the list
arr.append(60)

# Insert an element at a specific position
arr.insert(2, 25)

# Delete an element by its index
arr.pop(3)

# Print the final state of the array
print(arr)

# Search for a value in the array
arr = [1, 2, 3, 10]
if 10 in arr:
    print("Found 10 in the array")
