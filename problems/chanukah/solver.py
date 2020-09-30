import sys
# Solution for Kattis problem chanukah
# Problem url: https://open.kattis.com/problems/chanukah

# Sample-data#sample01.ans#sample01.in

P = int(sys.stdin.readline().strip())

for i in range(1,P+1):
    (N,K) = map(int, sys.stdin.readline().strip().split(" "))
    candles_lit = 0
    for j in range(1,K+1):
        candles_lit += j+1
    print(f"{i} {candles_lit}")