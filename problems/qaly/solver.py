import sys

n = int(sys.stdin.readline())

qual = 0.0
for line in sys.stdin.readlines():
    q, y = line.strip().split(" ")

    qual = qual + float(q)*float(y)

print("%.3f" % qual)

