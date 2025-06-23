# Given an array arr of n integers,
# the task is to find the largest element in the given array.

def findlargest(a):
    largest = a[0]
    for i in range(len(a)):
        if a[i] > largest:
            largest = a[i]
    return largest

a = [10, 33, 21, 78, 12]
res = findlargest(a)
print(res)

# Follows an Iterative Approach
# Time Complexity -> O(n)
# This time cannot be reduced for finding largest element in an unsorted array.
# O(n) remains the best time complexity that can be achieved.

# The same question can be solved using Recursion
def findlargest(a):
    if len(a) == 1:
        return a[0]
  else:
        return max(a[0], largest(a[1:]))
      
a = [10, 33, 21, 78, 12]
res = findlargest(a)
print(res)
