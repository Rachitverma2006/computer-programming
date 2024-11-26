# The RPS world championship is here. Here two players A and B play the game. You need to determine who wins.
# Both players can choose moves from the set {R,P,S}.
# The game is a draw if both players choose the same item.
# The winning rules of RPS are given below:
#
# Rock crushes scissor
# Scissor cuts paper
# Paper envelops rock


def gameResult(st):
    s = []
    for i in st:
        s.append(i)

    if s[0] == s[1]:
        s = "DRAW"
    elif s[0] == "R" and s[1] == "P":
        s = "B"
    elif s[0] == "R" and s[1] == "S":
        s = "A"
    elif s[0] == "P" and s[1] == "S":
        s = "B"
    elif s[0] == "P" and s[1] == "R":
        s = "A"
    elif s[0] == "S" and s[1] == "R":
        s = "B"
    elif s[0] == "S" and s[1] == "P":
        s = "A"
    elif s[0] == "P" and s[1] == "R":
        s = "A"
    elif s[0] == "S" and s[1] == "R":
        s = "B"
    elif s[0] == "S" and s[1] == "P":
        s = "A"
    elif s[0] == "R" and s[1] == "P":
        s = "B"
    elif s[0] == "P" and s[1] == "S":
        s = "B"
    elif s[0] == "R" and s[1] == "S":
        s = "A"
    return s


print(gameResult("RS"))
