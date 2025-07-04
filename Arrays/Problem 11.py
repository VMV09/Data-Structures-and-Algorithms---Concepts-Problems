# Given an array of n element, check if the array is sorted or not. 
# If sorted return True else return False
# It must return True, if it sorted in either ascending or descending order.
def checkifsorted(nums):
  n = len(nums)
  ascending = ascendings(nums, n)
  descending = descendings(nums, n)
  if ascending == True or descending == True:
    return True
  else:
    return False

def ascendings(nums, n):
  for i in range(n-1):
    if nums[i] < nums[i+1]:
      ascending = True
      return ascending

def descendings(nums, n):
  for i in range(n-1):
    if nums[i] > nums[i+1]:
      descending = True
      return descending

nums = [5, 4, 3, 2, 1]
checkifsorted(nums)
# You can design your own test cases to check the validity and correctness of the code.
# A much better and optimised way can be proposed to this exisitng solution.
