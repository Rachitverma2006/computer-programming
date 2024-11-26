# Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

# Note: 1-based indexing is followed here.


def search(k: int, arr: list[int]) -> int:
    # code here
    if k in arr:
        return arr.index(k) + 1
    else:
        return -1


print(search(2, [5, 8, 2, 4, 5, 2]))
