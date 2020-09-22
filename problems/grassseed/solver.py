import sys
# Solution for Kattis problem grassseed
# Problem url: https://open.kattis.com/problems/grassseed

# Sample-data#2.ans#1.in#2.in#1.ans

cost = float(sys.stdin.readline())
L = int(sys.stdin.readline())

total = 0
for _ in range(L):
    (Wi,Li) = sys.stdin.readline().split(" ")
    total += float(Wi)*float(Li)

print(f"{(total*cost):.7f}")

