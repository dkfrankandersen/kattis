import sys
# Solution for Kattis problem batterup
# Problem url: https://open.kattis.com/problems/batterup

# Sample-data#2.ans#1.in#3.in#2.in#3.ans#1.ans

n = int(sys.stdin.readline().strip())
bats = map(int,sys.stdin.readline().strip().split())

result = 0
substract = 0
for v in bats:
    if v >= 0:
        result += v
    else:
        substract +=1
        
print(result/(n-substract))