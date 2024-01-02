"""
Find Missing Number: Given an array of `n` numbers ranging from `1` to `n+1` with no duplicates,
find the missing number- solved By Adnan

"""


def FindMissingNumber(arr):
    n = len(arr)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number


# test

arr = [1, 2, 4, 5]
print(FindMissingNumber(arr))
print(type(FindMissingNumber(arr)))


