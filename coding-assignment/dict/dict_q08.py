# Create a function that merges two dictionaries, summing the values for any keys that appear in both dictionaries.

def merge_dicts_sum(dict1, dict2):
    merged = {**dict1}
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

print(merge_dicts_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}))
