import sys
# Solution for Kattis problem cetvrta
# Problem url: https://open.kattis.com/problems/cetvrta

# Sample-data#2.ans#1.in#2.in#1.ans

xs = []
ys = []

for _ in range(3):
    x, y = sys.stdin.readline().strip().split(" ")
    if x in xs:
        xs.remove(x)
    else:
        xs.append(x)
    if y in ys:
        ys.remove(y)
    else:
        ys.append(y)

print(f"{xs[0]} {ys[0]}")