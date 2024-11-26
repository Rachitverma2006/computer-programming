# Create a function that returns a tuple containing all factors of a number.
def tuple_of_factors(n):
    return tuple(i for i in range(1, n+1) if n % i == 0)


print(tuple_of_factors(12))
