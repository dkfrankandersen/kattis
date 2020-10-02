import sys
# Solution for Kattis problem autori
# Problem url: https://open.kattis.com/problems/autori

# Sample-data#autori.2.in#autori.3.ans#autori.1.in#autori.2.ans#autori.1.ans#autori.3.in

name = sys.stdin.readline().strip()

short = name[0]

for i in range(1, len(name)):
    if (name[i] == "-"):
        short += name[i+1]
    
print(short)