import sys

# Solution for Kattis problem parking2
# Problem url: https://open.kattis.com/problems/parking2

# Sample-data files
# parking.ans
# parking.in

T =  int(sys.stdin.readline())

for _ in range(0,T):
    noOfStores =  int(sys.stdin.readline())
    positions = map(int, sys.stdin.readline().strip().split(" "))
    sortedPos = sorted(positions)
    dist = 0
    for i in range(0, noOfStores-1):
        dist += sortedPos[i+1]-sortedPos[i]
    print(dist*2)
