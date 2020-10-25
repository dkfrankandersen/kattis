import sys

# Solution for Kattis problem jobexpenses
# Problem url: https://open.kattis.com/problems/jobexpenses

# Sample-data files
# 01.ans
# 01.in
# 02.ans
# 02.in
# 03.ans
# 03.in

N = int(sys.stdin.readline())
values = sys.stdin.readline().split(" ")

total = 0
for val in values:
    if val == "":
        continue
    v = int(val.strip())
    if v<0:
        total -= v
print(total)