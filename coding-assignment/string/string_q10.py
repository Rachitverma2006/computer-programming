# Given two strings S1 and S2 . Return "1" if both strings are anagrams otherwise return "0" .


def areAnagram(S1, S2):
    s1 = []
    s2 = []
    for i in S1:
        s1.append(i)
    for i in S2:
        s2.append(i)

    s1.sort()
    s2.sort()

    if s1 == s2:
        return 1
    else:
        return 0


print(areAnagram("silent", "listen"))
