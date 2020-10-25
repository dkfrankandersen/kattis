import sys

# Solution for Kattis problem numberfun
# Problem url: https://open.kattis.com/problems/numberfun

# Sample-data files
# sample01.ans
# sample01.in

def check(a,b,c):
    if (a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c):
        print("Possible")
    else:
        print("Impossible")

N = int(sys.stdin.readline())

for line in sys.stdin.readlines():
    a,b,c = map(int, line.strip().split(" "))
    check(a,b,c)