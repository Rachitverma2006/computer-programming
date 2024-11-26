# Create a function that returns a dictionary with characters as keys and their ASCII values as values.

def ascii_dict(s):
    return {char: ord(char) for char in s}

print(ascii_dict("abc"))
