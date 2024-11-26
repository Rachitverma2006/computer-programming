# Create a function that returns a tuple containing the squares of numbers from 1 to n.
def tuple_of_squares(n):
    x = tuple(x**2 for x in range(1, n+1))
    return x


print(tuple_of_squares(5))
