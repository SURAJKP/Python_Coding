# nums = [2,7,11,15], target = 9
# output = [0,1]    # Because 2 + 7 = 9

# array is a normal list behaves like a dynamic array
#normal key operations are delete, insert, update, search

def twoSum(nums, target):
    num_map = {}  # Dictionary to store the complement and its index

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
 
    return []  # Return an empty list if no solution is found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]  