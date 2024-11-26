# Create a function that returns a dictionary with numbers as keys and their factorials as values.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def dict_of_factorials(lst):
    return {x: factorial(x) for x in lst}

print(dict_of_factorials([1, 2, 3, 4, 5]))
