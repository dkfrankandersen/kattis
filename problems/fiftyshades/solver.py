import sys

# Solution for Kattis problem fiftyshades
# Problem url: https://open.kattis.com/problems/fiftyshades

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in

N = int(sys.stdin.readline())

found = 0
for _ in range(N):
    word = sys.stdin.readline().strip().lower()
    i = 0
    if "pink" in word or "rose" in word:
        found += 1

print( found if found > 0 else "I must watch Star Wars with my daughter")
