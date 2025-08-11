# Pair Sum in a Sorted and Rotated Array
def findPair(arr):
  i = 0
  for i in range(len(arr)):
    complement = arr[i] - target
    if complement == arr[i]:
      return true
  return false
  
