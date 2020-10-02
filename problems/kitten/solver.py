import sys
# Solution for Kattis problem kitten
# Problem url: https://open.kattis.com/problems/kitten

# Sample-data#test0.in#test0.ans

kitten = int(sys.stdin.readline().strip())
paths = dict()

for line in sys.stdin.readlines():
    if line .strip() == "-1":
        break
    
    values = list(map(int, line.strip().split(" ")))
    
    a = values[0]
    bs = values[1:]

    for v in bs:
        paths[v] = a

v = kitten
path = str(v)
while (v in paths):
    if v in paths: 
        v = paths[v]
        path += " "
        path += str(v)
print(path)    