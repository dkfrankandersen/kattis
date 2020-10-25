import sys

# Solution for Kattis problem licensetolaunch
# Problem url: https://open.kattis.com/problems/licensetolaunch

# Sample-data files
# 1.ans
# 1.in

N = int(sys.stdin.readline())
spaceJunkAtDay = list(map(int, sys.stdin.readline().strip().split(" ")))

bestJunkDay = (0,max(spaceJunkAtDay)+1) # (junk amount, at day)
for i in range(0,N):
    if spaceJunkAtDay[i] < bestJunkDay[1]:
        bestJunkDay = (i, spaceJunkAtDay[i])

print(bestJunkDay[0])