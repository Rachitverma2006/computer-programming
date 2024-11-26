# You will be given two numbers a and b in form of string. Your task is to print 1 if a < b, print 2 if a > b and print 3 if a = b.


def check(a, b):

    if int(a) == int(b):
        return 3
    elif int(a) > int(b):
        return 2
    else:
        return 1


print(check(2, 5))
