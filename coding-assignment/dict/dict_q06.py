# write a program to find find common keys in two dictionaries.

def common_keys(dict1, dict2):
    return set(dict1.keys()) & set(dict2.keys())

print(common_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))
