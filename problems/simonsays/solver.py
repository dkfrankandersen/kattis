import sys

# Solution for Kattis problem simonsays
# Problem url: https://open.kattis.com/problems/simonsays

# Sample-data files
# 01_simple.ans
# 01_simple.in
# 02_simple.ans
# 02_simple.in
# 03_simple.ans
# 03_simple.in

N = int(sys.stdin.readline())

for i in range(0,N):
    line = sys.stdin.readline().strip()
    if line.startswith("Simon says"):
        print(line.replace("Simon says ", ""))