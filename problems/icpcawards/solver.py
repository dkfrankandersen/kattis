import sys

# Solution for Kattis problem icpcawards
# Problem url: https://open.kattis.com/problems/icpcawards

# Sample-data files
# 1.ans
# 1.in

N = int(sys.stdin.readline())

unis = dict() 
for _ in range(0,N):
    uni, team = sys.stdin.readline().strip().split(" ")

    if len(unis) >= 12:
        break

    if uni not in unis:
        unis[uni] = 1
        print(f"{uni} {team}")