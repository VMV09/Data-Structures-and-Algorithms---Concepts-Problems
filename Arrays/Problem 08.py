# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
#     rotate 1 steps to the right: [7,1,2,3,4,5,6]
#     rotate 2 steps to the right: [6,7,1,2,3,4,5]
#     rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# Design your own test cases to check and verify the working of the code

for i in range(k):
    n = nums.pop()           # pop last element
    nums.insert(0, n)        # insert at beginning

print(nums)
