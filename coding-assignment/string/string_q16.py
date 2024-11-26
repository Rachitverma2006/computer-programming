# You are given a string S, convert it into a magical string.
# A string can be made into a magical string if the alphabets are swapped in the given manner: a->z or z->a, b->y or y->b, and so on.


# Note: All the alphabets in the string are in lowercase.


def magicalString(s):
    a = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    b = sorted(a)
    b.reverse()
    c = ""
    for i in s:
        m = a.index(i)
        c += b[m]
    return c


print(magicalString("abcde"))
