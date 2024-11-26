# write a program that takes a dictionary as input and return the key which has minimum value.

def min_value_key(d):
    return min(d, key=d.get)

print(min_value_key({"a": 1, "b": 2, "c": 3}))
