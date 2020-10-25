import sys
import itertools

# Solution for Kattis problem kornislav
# Problem url: https://open.kattis.com/problems/kornislav

# Sample-data files
# kornislav.1.ans
# kornislav.1.in
# kornislav.2.ans
# kornislav.2.in

def allPermutations(lst):
    return list(itertools.permutations(lst,4))

def isCuttingFirstLine(coords):
    a,b,c,d = coords
    if 0>=d[1] and d[0]>=0:
        return True
    else:
        return False

def findMaxArea(steps):
    permutations = allPermutations(sorted(steps))
    maxArea = 0
    for a,b,c,d in permutations:
        coords = []
        x,y = (a,0) # right
        coords.append((x,y))
        x,y = (x,b) # up
        coords.append((x,y))
        x,y = (x-c,y) # left
        coords.append((x,y))
        x,y = (x,y-d) # down
        coords.append((x,y))

        if isCuttingFirstLine(coords):
            if b*c>maxArea:
                maxArea = b*c
    return maxArea

steps = list(map(int, sys.stdin.readline().split(" ")))
result = findMaxArea(steps)
print(result)