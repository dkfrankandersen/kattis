import sys
# Solution for Kattis problem trik
# Problem url: https://open.kattis.com/problems/trik

# Sample-data#2.ans#1.in#2.in#1.ans

cups = {1:"A", 2:"B", 3:"C"}

moves = sys.stdin.readline().strip()

def moveCup(F,T):
    a = cups[F]
    b = cups[T]
    cups[F] = b
    cups[T] = a

for to in moves:
    if to == "A":
        moveCup(1,2)
    if to == "B":
        moveCup(2,3)
    if to == "C":
        moveCup(1,3)

for k in cups.keys():
    if cups[k] == "A":
        print(k)