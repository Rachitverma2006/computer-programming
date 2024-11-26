# Create a function that checks if the elements of a tuple form a palindrome.
def is_tuple_palindrome(tpl):
    return tpl == tpl[::-1]

print(is_tuple_palindrome((1, 2, 3, 2, 1)))
