# Given a string s consisting of only '0's and '1's,  find the last index of the '1' present.

# Note: If '1' is not present, return "-1"\


def lastIndex(s: str) -> int:
    m = s.rfind("1")
    return m


s = "01101"
print(lastIndex(s))
