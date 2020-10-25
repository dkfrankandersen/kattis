import sys

# Solution for Kattis problem pokerhand
# Problem url: https://open.kattis.com/problems/pokerhand

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in
# 3.ans
# 3.in

hands = sys.stdin.readline().strip().split(" ")

ranks = dict()
for hand in hands:
    rank = hand[:1]
    if rank not in ranks:
        ranks[rank] = 1
    else:
        ranks[rank] +=1

value = 0
for rankVal in ranks.values():
    if rankVal > value:
        value = rankVal
print(value)