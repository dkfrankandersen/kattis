import sys

# Solution for Kattis problem judgingmoose
# Problem url: https://open.kattis.com/problems/judgingmoose

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in
# 3.ans
# 3.in

l,r = map(int, sys.stdin.readline().split(" "))

if l>0 or r>0:
    if l==r:
        print(f"Even {l+r}")
    else:
        print(f"Odd {max(l,r)*2}")
else:
    print("Not a moose")