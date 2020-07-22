import sys

s1, s2 = sys.stdin.readline().split(" ")

r1 = s1[::-1].strip()
r2 = s2[::-1].strip()

if int(r1) > int(r2):
    print (r1)
else:
    print (r2)