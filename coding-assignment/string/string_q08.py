# Given a string s consisting of upper/lower-case alphabets and empty space characters ‘ ‘. The string may contain spaces at the end. You will have return the length of last word which consists of alphabets only.


def findLength(s):
    st = s.split()
    c = st[-1]
    l = len(c)
    return l


print(findLength("hello world this is python"))
