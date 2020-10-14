import sys
# Solution for Kattis problem tarifa
# Problem url: https://open.kattis.com/problems/tarifa

# Sample-data#tarifa.1.ans#tarifa.2.in#tarifa.3.ans#tarifa.3.in#tarifa.2.ans#tarifa.1.in

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

saved = X

for line in sys.stdin.readlines():
    p = int(line)
    if p <= saved:
        saved += X-p

print(saved)