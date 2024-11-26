# You are given a string S. Your task is to determine if the sum of ASCII values of all character results in a perfect square or not. If it is a perfect square then the answer is 1, otherwise 0.

import math


def isSquare(s):
    c = 0
    for i in s:
        c += ord(i)

    m = math.sqrt(c)
    m = str(m)
    i = m.index(".")
    m = m[i + 1 :]

    if len(m) > 1:
        return 0
    else:
        return 1


print(isSquare("64"))
