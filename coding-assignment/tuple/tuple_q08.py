# Create a function that filters out even numbers from a tuple.
def filter_even_numbers(tpl):
    t = tuple(x for x in tpl if x % 2 == 0)
    return t


print(filter_even_numbers((1, 2, 3, 4, 5, 6)))
