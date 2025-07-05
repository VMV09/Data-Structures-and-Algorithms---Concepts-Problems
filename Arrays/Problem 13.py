# Given an array with n elements, move all the zeros to the end of the array.
# Input: nums = [0, 1, 0, 3, 12]
# Output: nums = [1, 3, 12, 0, 0]

def moveZeroes(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1):
            if nums[j] == 0 and nums[j + 1] != 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
