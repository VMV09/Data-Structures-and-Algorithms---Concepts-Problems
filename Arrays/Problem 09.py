# Given an array of integers arr, find the second larget element in the array.
# Two Pass Search => In the first traversal, we find maximum element
# second traversal we find maximum element ignoring the one we found in the
# first traversal

# Time Complexity => O(2*n); as we are traversing array two times

def secondlargest(arr):
  n = len(arr)
  largest = -1
  secondlargest = -1
  for i in range(n):
    if arr[i] > largest:
      largest = arr[i]

  for i in range(n):
    if arr[i] > secondlargest and arr[i] != largest:
      secondlargest = arr[i]
  return secondlargest

arr = [10, 3, 5, 9, 12, 16, 17]
res = secondlargest(arr)
print(res)

# The same question can be solved using a one pass search with two pointers.
# Time Complexity => O(n); as we will only traverse the array once and keep a track of largest and secondlargest.
def secondlargest(arr):
  n = len(arr)
  largest = -1
  secondlargest = -1
  for i in range(n):
    if arr[i] > largest:
      secondlargest = largest
      largest = arr[i]
    elif arr[i] < largest and arr[i] > secondLargest:
      secondLargest = arr[i]
  return secondlargest

arr = [10, 3, 5, 9, 12, 16, 17]
res = secondlargest(arr)
print(res)
