import sys

# Solution for Kattis problem freefood
# Problem url: https://open.kattis.com/problems/freefood

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in
# 3.ans
# 3.in

N = int(sys.stdin.readline())

days = dict()

for i in range(N):
    s, t = map(int, sys.stdin.readline().strip().split())
    for j in range(s,t+1):
        days[j] = True

print(len(days))