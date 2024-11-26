# You are given an array arr. Find the sum of distinct elements in an array.


def findSum(arr):
    a = sum(list(set(arr)))
    return a


print(findSum([2, 5, 4, 7, 7, 8, 8, 5, 9, 6, 4, 1]))
