# Given an Array with N elements, check if the element is present or not.
# If present return the index of the element else -1

def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

arr = [10, 20, 30, 40, 50]
x = 30
N = len(arr)

# Function call
result = search(arr, N, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

# You can define your own Test Cases and Check the working and correctness of the code.
