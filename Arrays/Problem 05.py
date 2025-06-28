# Given an array arr, reverse the elements in the array.
# input: arr = [1, 2, 3, 4, 5]
# output: arr = [5, 4, 3, 2, 1]

def reverse(a):
    i = 0
    j = len(a) - 1
    while i <= j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
    print(a)

a = [1, 2, 3, 4, 5]
print('Before Reversal')
print(a)
print('After Reversal')
reverse(a)

# You can frame your own test cases to check and verify the correctness and functionality of the code.
