import sys
# Solution for Kattis problem modulo
# Problem url: https://open.kattis.com/problems/modulo

# Sample-data#2.ans#1.in#3.in#2.in#3.ans#1.ans

distinct = set()
for i in sys.stdin.readlines():
    distinct.add(int(i)%42)

print(len(distinct))