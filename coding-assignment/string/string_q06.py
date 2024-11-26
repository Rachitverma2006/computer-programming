# Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.


def RedOrGreen(s):
    c = 0
    r = s.count("R")
    g = s.count("G")
    for i in s:
        if r > g:
            if i == "G":
                c += 1
        else:
            if i == "R":
                c += 1
    return c


print(RedOrGreen("RGRRGGR"))
