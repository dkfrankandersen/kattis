import sys
# Solution for Kattis problem bela
# Problem url: https://open.kattis.com/problems/bela

# Sample-data#bela.1.ans#bela.2.in#bela.1.in#bela.2.ans

scores = {
            "A":[11,11],
            "K":[4,4],
            "Q":[3,3],
            "J":[20,2],
            "T":[10,10],
            "9":[14,0],
            "8":[0,0],
            "7":[0,0]}

(N,B) = sys.stdin.readline().strip().split(" ")

points = 0
for card in sys.stdin.readlines():
    if card[1]==B:
        points += scores[card[0]][0]
    else:
        points += scores[card[0]][1]

print(points)