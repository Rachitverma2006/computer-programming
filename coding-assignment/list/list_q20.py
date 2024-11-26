# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.


def get_min_max(arr):
    arr.sort()
    mi = arr[0]
    ma = max(arr)
    x = [mi, ma]
    return x


print(get_min_max([1, 2, 8, 9, 6]))
