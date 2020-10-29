import sys

# Solution for Kattis problem isithalloween
# Problem url: https://open.kattis.com/problems/isithalloween

# Sample-data files
# 1.ans
# 1.in
# 2.ans
# 2.in

date = sys.stdin.readline().strip()

if date == "OCT 31" or date == "DEC 25":
    print("yup")
else:
    print("nope")