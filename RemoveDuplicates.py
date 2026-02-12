def removeDuplicates(arr):
    if len(arr) == 0:
        return 0

    # Initialize the index of the next unique element
    unique_index = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If the current element is different from the previous one
        if arr[i] != arr[i - 1]:
            # Move the unique element to the unique_index position
            arr[unique_index] = arr[i]
            unique_index += 1

    # Return the number of unique elements
    return unique_index

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = removeDuplicates(arr)
print("New length of the array after removing duplicates:", new_length)
print("Array after removing duplicates:", arr[:new_length])