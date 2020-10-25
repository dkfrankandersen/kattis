import sys
import math
# Solution for Kattis problem ladder
# Problem url: https://open.kattis.com/problems/ladder

# Sample-data files
# ladder.00.ans
# ladder.00.in
# ladder.01.ans
# ladder.01.in

h,v = map(int, sys.stdin.readline().split(" "))
c = h/math.sin(math.radians(v))
c = int(c+1) if c > int(c) else int(c)
print(c)
