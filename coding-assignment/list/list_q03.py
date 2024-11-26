# You are given an array arr. You need to print elements of arr in alternate order (starting from index 0).


def printAl(arr):
    for i in range(1, len(arr) + 1):
        if i % 2 != 0:
            print(arr[i - 1], end=" ")


print(printAl([2, 5, 8]))
