# Create a function that returns the sum of all elements in a nested tuple.
def nested_tuple_sum(tpl):
    total = 0
    for item in tpl:
        if isinstance(item, tuple):
            total += nested_tuple_sum(item)
        else:
            total += item
    return total


print(nested_tuple_sum((1, (2, 3), (4, (5, 6)))))
