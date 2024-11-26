# Given an unsorted array arr. Find the count of elements less than or equal to the given element x.


def countOfElements(x, arr):
    arr.sort()
    c = 0
    for i in arr:
        if i <= x:
            c += 1
    return c


print(countOfElements(5, [1, 2, 4, 7, 85]))
