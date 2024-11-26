# Given string str of a constant length, print a triangle out of it. The triangle should start with the first character of the string and keep growing downwards by adding one character from the string.
# The spaces on the left side of the triangle should be replaced with a dot character.


def printTriangleDownwards(s):
    # code here
    d = len(s)
    rows = len(s)
    for i in range(1, d + 1):
        for j in range(d - i):
            print(".", end="")
        for j in range(i):
            print(s[j], end="")
        print()


printTriangleDownwards("GLA UNIVERSITY")
