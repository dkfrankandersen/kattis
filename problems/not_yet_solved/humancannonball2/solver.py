import sys
import math
# Solution for Kattis problem humancannonball2
# Problem url: https://open.kattis.com/problems/humancannonball2

# Sample-data#test0.in#test0.ans

n = sys.stdin.readline()

for line in sys.stdin.readlines():
    v0, theta, x1, h1, h2 = map(float, line.split(" "))

   
    t = 0.85

    y = v0*t*math.sin(theta)-(0.5*9.81*(t**2))
    t = x1/(v0*math.cos(theta))

    print((v0, theta, x1, h1, h2))
    print(f"t: {t}")
    # print(f"x: {x}")
    print(f"y: {y}")
    result = y > (h1+1.0) and y < (h2-1.0)
    print("Safe" if result else "Not Safe")