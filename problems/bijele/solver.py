import sys
# Solution for Kattis problem bijele
# Problem url: https://open.kattis.com/problems/bijele

# Sample-data#2.ans#1.in#2.in#1.ans


pieces_found = map(int, sys.stdin.readline().strip().split(" "))

pieces_found = list(pieces_found)
# kings, queens, rooks, bishops, knights and pawns
    # One king
    # One queen
    # Two rooks
    # Two bishops
    # Two knights
    # Eight pawns

pieces_inset = [1,1,2,2,2,8]

result = ""
for i in range(6):
    if (pieces_found[i] == pieces_inset[i]):
        result += " 0"
    else:
        result += " "
        result += str(pieces_inset[i]-pieces_found[i])


print(result.lstrip(" "))
    