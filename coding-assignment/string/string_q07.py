# Given a list of characters, merge all of them into a string.


def chartostr(arr):
    # code here
    s = ""
    for i in arr:
        s += i
    return s


print(chartostr(["H", "E", "L", "L", "O"]))
