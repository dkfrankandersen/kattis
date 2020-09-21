import sys
# Solution for Kattis problem nastyhacks
# Problem url: https://open.kattis.com/problems/nastyhacks

# Sample-data#1.in#1.ans

n = sys.stdin.readline()

for l in sys.stdin.readlines():
    # r is the expected revenue if you do not advertise,
    # e is the expected revenue if you do advertise 
    # c is the cost of advertising

    (R, E, C) = l.strip().split(" ")
    
    r = int(R)
    e = int(E)
    c = int(C)

    if (r < (e-c)):
        print("advertise")
    elif(r == (e-c)):
        print("does not matter")
    else:    
        print("do not advertise")
