#Create a function that rotates the elements of a tuple by k positions to the right.
def rotate_tuple(tpl, k):
    k = k % len(tpl)
    return tpl[-k:] + tpl[:-k]


print(rotate_tuple((1, 2, 3, 4, 5), 2))