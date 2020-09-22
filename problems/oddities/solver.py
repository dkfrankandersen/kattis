import sys
# Solution for Kattis problem oddities
# Problem url: https://open.kattis.com/problems/oddities

# Sample-data#sample.ans#sample.in

n = sys.stdin.readline()

for l in sys.stdin.readlines():
    x = int(l.strip())
    odd_even = "odd"
    if x % 2 == 0:
        odd_even = "even"

    print(f"{x} is {odd_even}")