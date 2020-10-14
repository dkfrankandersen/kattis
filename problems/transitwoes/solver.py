import sys
# Solution for Kattis problem transitwoes
# Problem url: https://open.kattis.com/problems/transitwoes

# Sample-data#transitwoes-01.ans#transitwoes-02.ans#transitwoes-02.in#transitwoes-01.in

s,t,n = map(int, sys.stdin.readline().strip().split(" "))

def readToIntList():
    return list(map(int, sys.stdin.readline().strip().split(" ")))

ds = readToIntList()
bs = readToIntList()
cs = readToIntList()

travelTime = 0

# print(f"Leaves home: {s}, needs to be at class {t}")
for i in range(0,n+1):
    travelTime += ds[i]
    # print(f"d_{i}: Time spend on walk to bus, {travelTime}")
    
    if i>0 and i<=n:
        travelTime += bs[i-1]
        # print(f"b_{i}: Time spend on bus, {travelTime}")
    
    if i<n:
        if travelTime <= cs[i-1]:
            m = cs[i] - travelTime
        else:
            m = travelTime % cs[i]
        travelTime += m
        # print(f"c_{i}: Time spend bus, interval wait {travelTime}")

result = "yes" if s+travelTime <= t else "no"

# print(travelTime)
print(result)