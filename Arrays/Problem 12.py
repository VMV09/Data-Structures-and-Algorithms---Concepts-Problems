# Given an array arr[] of size n, the task is to find all the Leaders in the array. 
# An element is a Leader if it is greater than or equal to all the elements to its right side.
# Note: The rightmost element is always a leader.

# My Solution
# Two pointer approach => i = a[0]; j = a[1]

# a = [16, 17, 4, 3, 5, 2, 6, 7, 8, -1] => Proper Execution
# a = [i for i in range(10000000, 0, -1)] => Proper Execution
# a = [10, 10, 5, 2, 10, 1] => Proper Execution
# a = [5, 4, 3, 2, 1] => Proper Execution
def leaderelement(a):
  n = len(a)
  i = 0
  j = 1
  while i < n and j < n:
    if a[i] >= a[j]:
      j = j + 1
    elif i <= j:
      i = i + 1
      j = i + 1
    if j == n:
      print(a[i], end = " ")
      i += 1
      j = i + 1
  if i == n-1:
    print(a[i])
  #print(a[-1])

leaderelement(a)
