# Create a function that returns a tuple with unique elements from the input tuple.
def unique_elements(tpl):
    return tuple(set(tpl))


print(unique_elements((1, 2, 3, 2, 1, 4, 5)))
