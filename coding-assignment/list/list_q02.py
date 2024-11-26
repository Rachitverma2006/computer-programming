# Given an array arr[]. The task is to find the largest element and return it.
def largest(arr: list[int]) -> int:
    # code here
    c = 0
    for i in arr:
        if i > c:
            c = i
    return c


print(largest([1, 2, 8, 3, 4, 5]))
