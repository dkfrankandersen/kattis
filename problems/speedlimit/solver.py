import sys
# Solution for Kattis problem speedlimit
# Problem url: https://open.kattis.com/problems/speedlimit

# Sample-data#sample.ans#sample.in

while(True):
    v = list(map(int, sys.stdin.readline().strip().split(" ")))
    if len(v) == 1:        
        if v[0]==-1:
            break
        dist = 0
        last = 0
        for _ in range(0, v[0]):
            s, e = map(int, sys.stdin.readline().strip().split(" "))

            dist += s*(e-last)
            last = e

        print(f"{dist} miles")