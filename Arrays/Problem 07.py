# Problem: Given an array of integers, find the maximum sum of a contiguous subarray where the elements are in strictly ascending order.
def MaximumAscendingSubArray(a):
    current_sum = a[0]
    max_sum = a[0]
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            current_sum = current_sum + a[i]
        else:
            current_sum = a[i]
    max_sum = max(max_sum, current_sum)
    return max_sum

a = [10, 20, 30, 50, 5, 10, 100]
res = MaximumAscendingSubArray(a)
print(res)

# Design your own testcases to check and verify the correctness of the code designed.
