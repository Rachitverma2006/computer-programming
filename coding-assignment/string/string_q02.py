# Given two strings string1 and string2, remove those characters from first string(string1) which are present in second string(string2). Both the strings are different and contain only lowercase characters.


def removeChars(string1, string2):
    c = ""
    for i in string1:
        if i in string2:
            pass
        else:
            c += i
    return c


print(removeChars("hello", "mouse"))
