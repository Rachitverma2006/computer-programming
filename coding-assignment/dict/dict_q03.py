# Write a program to make a dictionary from two lists.

def create_dict(keys, values):
    return dict(zip(keys, values))

print(create_dict(["a", "b", "c"], [1, 2, 3]))
