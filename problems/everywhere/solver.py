import sys
# Solution for Kattis problem everywhere
# Problem url: https://open.kattis.com/problems/everywhere

# Sample-data#everywhere-01.in#everywhere-01.ans

n = int(sys.stdin.readline())

for _ in range(n):
    t = int(sys.stdin.readline())
    cities = set()
    for _ in range(t):
        city = sys.stdin.readline().strip()
        cities.add(city)
    print(len(cities))