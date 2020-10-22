import sys

# Solution for Kattis problem railroad2
# Problem url: https://open.kattis.com/problems/railroad2

# Sample-data files
# sample003.ans
# sample002.ans
# sample003.in
# sample001.in
# sample001.ans
# sample002.in

junctions, switches = map(int, sys.stdin.readline().split(" "))

if junctions <= 1 and switches == 0:
    res = 1
elif junctions >= 0 and switches % 2 == 0:
    res = 1
else:
    res = 0

if res > 0:
    print("possible")
else:
    print("impossible")