# Given an array with replicates, check if it contains any duplicates.
def contains_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage
arr = [1, 2, 3, 4, 5, 1]
res = contains_duplicates(arr)
print("Contains duplicates:", res)

# You can design your own testcases to check and verify the correctness of the code.
