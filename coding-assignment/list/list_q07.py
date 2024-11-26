# Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

# Note: Return an array of two elements where the first one in the count of odd & second one is the count of even.


def countOddEven(arr):
    o = 0
    e = 0
    for i in arr:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    l = [o, e]
    return l


print(countOddEven([2, 4, 5, 8, 6, 9, 7]))
