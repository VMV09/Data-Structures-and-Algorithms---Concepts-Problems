# Given an array arr[], the task is to find the top three largest distinct integers present in the array.
# Note: If there are less than three distinct elements in the array, then return the available distinct numbers in 
# descending order.
# My Solution

# Three pass Search => In the first traversal, we find maximum element
# second traversal we find maximum element ignoring the one we found in the
# first traversal
# third traversal we find maximum element ignoring the one we found in the first
# and second traversal

# Time Complexity => O(3*n)
a = [10, 4, 3, 50, 23, 90]
# Check with inputs => [10, 9, 9] and [10, 10, 10]

def largestthree(a):
  n = len(a)

  largest = -1
  secondlargest = -1
  thirdlargest = -1

  for i in range(n):
    if a[i] > largest:
      largest = a[i]

  for i in range(n):
    if a[i] > secondlargest and a[i] != largest:
      secondlargest = a[i]

  for i in range(n):
    if a[i] > thirdlargest and a[i] != largest and a[i] != secondlargest:
      thirdlargest = a[i]

  return largest, secondlargest, thirdlargest

res1, res2, res3 = largestthree(a)

if res1 != -1:
  print(res1, end = " ")
if res2 != -1:
  print(res2, end = " ")
if res3 != -1:
  print(res3, end = " ")
