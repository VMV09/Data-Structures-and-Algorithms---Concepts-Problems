nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

for i in range(k):
    n = nums.pop()           # pop last element
    nums.insert(0, n)        # insert at beginning

print(nums)
