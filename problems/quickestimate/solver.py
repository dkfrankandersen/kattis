import sys

# Solution for Kattis problem quickestimate
# Problem url: https://open.kattis.com/problems/quickestimate

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in

N = int(sys.stdin.readline())

for _ in range(0,N):
    print(len(sys.stdin.readline().strip()))