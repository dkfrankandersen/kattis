import sys


(N, H, V) = sys.stdin.readline().split(" ")

n = int(N)
h = int(H)
v = int(V)

p1 = (h) * (v) * 4
p2 = (n-h) * (v) * 4
p3 = (h) * (n-v) * 4
p4 = (n-h) * (n-v) * 4

volume = max(p1,p2,p3,p4)
 
print(volume)