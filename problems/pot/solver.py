import sys

n = sys.stdin.readline()

total_sum = 0
for line in sys.stdin.readlines():
    l = line.strip()
    N = l[:len(l)-1]
    P = l[len(l)-1:]
    total_sum += int(N)**int(P)

print(total_sum)