# Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces.


def reverseString(s):

    s = s[::-1]
    reg = ""

    for i in s:
        if i == " ":
            pass
        elif i not in reg:
            reg += i

    return reg


print(reverseString("hello world"))
