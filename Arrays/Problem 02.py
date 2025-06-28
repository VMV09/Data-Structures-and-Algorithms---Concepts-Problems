# LeetCode Problem - 
# Given an array nums and a target element
# Remove all occurance of the target element in the array.

def removeElement(a, val):
    i = 0
    while i < len(a):
        if a[i] == val:
            a.pop(i)
        else:
            i += 1
    print(a)

nums = [3, 2, 2, 3]
target = 3
removeElement(nums, target)
