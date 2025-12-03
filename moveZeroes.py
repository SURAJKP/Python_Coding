#Input:  [0,1,0,3,12]
#Output: [1,3,12,0,0]

def moveZeroes(nums):
    non_zero_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1

    while non_zero_pos < len(nums):
        nums[non_zero_pos] = 0
        non_zero_pos += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]