# Given an array arr, find the kth largest element in the array.
# Input: nums = [6, 2, 12, 89, 33]
#        k = 3
# Output: 12, it is the 3rd largest element.

# It is Important to know that there are more than one way to solve this problem.
# This file contains the easy approach first and the second approach is shown below in the same file, that uses core logic of arrays.
def kthlargest(arr, k):
  arr.sort(reverse=True)
  return arr[k-1]

arr = [6, 2, 12, 89, 33]
k = 3

---------------------------------------------------------------------------------------------------------------------------------
# Second Approach
# QuickSelect - This is an optimisation of the above method, if QuickSort is used as a sorting algorithm in first step.
# ALGORITHM 
#   a. Pick a Pivot point.
#   b. Partition the array into three parts:
#           - LeftArr = elements lesser than pivot
#           - MidArr = elements equal to pivot

import random

def quick_select(arr, k):
  
  pivot = random.choice(arr)
  print(pivot)

  leftArr = [x for x in arr if x > pivot]

  midArr = [x for x in arr if x == pivot]

  rightArr = [x for x in arr if x < pivot]

  if k <= len(leftArr):
    return quick_select(leftArr, k)
  if len(leftArr) + len(midArr) < k:
    return quick_select(rightArr, k - len(leftArr) - len(midArr))

  return pivot

def kth_largest(arr, k):
  return quick_select(arr, k)

if __name__ == "__main__":
  arr = [12, 3, 5, 7, 19]
  k = 2
  print(kth_largest(arr, k))
-----------------------------------------------------------------------------------------------------------------------------
