# Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.


def PalinArray(arr):
    c = True
    for i in arr:
        x = i
        r_d = 0
        while i:
            d = i % 10
            r_d = r_d * 10 + d
            i = i // 10
        if x == r_d:
            c = True
        else:
            c = False
            break
    if c == True:
        return c
    else:
        return c


print(PalinArray([1, 2, 1]))
