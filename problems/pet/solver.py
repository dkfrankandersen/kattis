import sys

# Solution for Kattis problem pet
# Problem url: https://open.kattis.com/problems/pet

# Sample-data files
# pet.1.ans
# pet.1.in
# pet.2.ans
# pet.2.in

winner = (0,0)
for i in range(1,6):
    line = sys.stdin.readline()
    pointsSum = sum(map(int, line.strip().split(" ")))
    if pointsSum > winner[1]:
        winner = (i, pointsSum)

print(f"{winner[0]} {winner[1]}")