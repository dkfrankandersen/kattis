import sys

# Solution for Kattis problem hangingout
# Problem url: https://open.kattis.com/problems/hangingout

# Sample-data files
# 1.ans
# 1.in

L,x = map(int, sys.stdin.readline().strip().split(" "))

notAllowedIn = 0
onTerrace = 0
for i in range(x):
    action, amount = sys.stdin.readline().strip().split(" ")
    amount = int(amount)
    if action == "enter":
        if amount <= L-onTerrace:
            onTerrace += amount
        else:
            notAllowedIn += 1
    
    if action == "leave":
        onTerrace -= amount
        if onTerrace < 0:
            onTerrace = 0
print(notAllowedIn) 