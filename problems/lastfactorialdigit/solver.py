import sys
# import math
# Solution for Kattis problem lastfactorialdigit
# Problem url: https://open.kattis.com/problems/lastfactorialdigit

# Sample-data#2.ans#1.in#2.in#1.ans

n = sys.stdin.readline()

for t in sys.stdin.readlines():
    t = int(t)
    # v = str(math.factorial(t)) Alternative
    v = 1
    for i in range(1,t+1):
        v = v*i
    print(str(v)[-1:])