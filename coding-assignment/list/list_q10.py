# You are given an integer n. You need to convert all zeroes of n to 5.


def convertFive(n):
    # Code here
    num = ""
    n = str(n)
    for i in n:
        if int(i) == 0:
            num += "5"
        else:
            num += i

    num = int(num)
    return num


print(convertFive(1054580))
