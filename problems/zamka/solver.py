import sys
# Solution for Kattis problem zamka
# Problem url: https://open.kattis.com/problems/zamka

# Sample-data#zamka.3.ans#zamka.3.in#zamka.1.in#zamka.1.ans#zamka.2.ans#zamka.2.in

def StdInLineToInt():
    return int(sys.stdin.readline().strip())

L = StdInLineToInt()
D = StdInLineToInt()
X = StdInLineToInt()

N = L
M = D

def digitsSumsTo(digits, sumsTo):
    s = 0
    for c in str(digits):
        s+=int(c)
    return s==sumsTo

for i in range(L,D):
    if digitsSumsTo(N, X):
        break
    else:
        N += 1

for j in range(L,D):
    if digitsSumsTo(M, X):
        break
    else:
        M += -1

print(N)
print(M)