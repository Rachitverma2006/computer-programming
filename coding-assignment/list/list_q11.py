# Given an array arr, swap the kth element from the beginning with the kth element from the end.

# Note: 1-based indexing is followed.


def swapKth(k, arr):

    arr[k - 1], arr[-k] = arr[-k], arr[k - 1]
    return arr


print(swapKth(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
