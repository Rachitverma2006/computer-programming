# Pappu is confused between 6 & 9. He works in the billing department of abc company and his work is to return the remaining amount to the customers. If the actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.


def findDiff(s):
    st = str(s)
    st2 = ""
    for i in st:
        if i == "6":
            st2 += "9"
        else:
            st2 += i
    st2 = int(st2)
    return st2 - s


print(findDiff(5446859))
