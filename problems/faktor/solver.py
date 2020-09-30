import sys
# Solution for Kattis problem faktor
# Problem url: https://open.kattis.com/problems/faktor

# Sample-data#faktor.dummy.3.ans#faktor.dummy.2.ans#faktor.dummy.2.in#faktor.dummy.1.in#faktor.dummy.3.in#faktor.dummy.1.ans


values = sys.stdin.readline().strip()
(A,I) = map(int,values.split(" "))

print((A*I)-A+1)