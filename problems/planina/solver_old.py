import sys

n = int(sys.stdin.readline())
print(n)

squares = 1
points = 4
for i in range(n):
    before = squares
    points += squares*5
    squares += squares*4
    
    
print()
print(squares)
print(points)