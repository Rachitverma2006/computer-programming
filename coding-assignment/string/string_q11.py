# Given a Sentence S of length N containing only english alphabet characters, your task is to write a program that converts the given sentence to Snake Case sentence. Snake case is the practice of writing compound words or phrases in which the elements are separated with one underscore character (_) and no spaces, and the first letter of each word written in lowercase. For ease keep all the characters in lowercase.


def snakeCase(s):

    m = s.lower()
    c = ""

    for i in m:
        if i == " ":
            c += "_"
        else:
            c += i
    return c


print(snakeCase("hello world"))
