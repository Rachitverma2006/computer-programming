# Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order.


def findElements(arr):
    for i in range(2):
        m = max(arr)
        arr.remove(m)
    arr.sort()
    return arr


print(findElements([2, 5, 4, 6, 9, 8]))
