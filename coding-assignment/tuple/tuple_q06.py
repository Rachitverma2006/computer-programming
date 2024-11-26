# Create a function that groups elements of a tuple into sub-tuples of length n.
def group_elements(tpl, n):
    return tuple(tpl[i:i + n] for i in range(0, len(tpl), n))


print(group_elements((1, 2, 3, 4, 5, 6, 7, 8), 3))
