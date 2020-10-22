import sys

# Solution for Kattis problem romans
# Problem url: https://open.kattis.com/problems/romans

# Sample-data files
# t1.in
# t1.ans
# t0.ans
# t0.in

miles = float(sys.stdin.readline())
romanPaces = int(miles*1000*(5280/4854)+0.5)
print(romanPaces)