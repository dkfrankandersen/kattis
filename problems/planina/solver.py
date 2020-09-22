import sys

n = int(sys.stdin.readline().strip())

def split(n,i,p):
    if (i>=n):
        print (p*p)
    else:
        p2 = p+(p-1)
        split(n,i+1,p2)

split(n,0,2)