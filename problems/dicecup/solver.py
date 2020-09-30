import sys
# Solution for Kattis problem dicecup
# Problem url: https://open.kattis.com/problems/dicecup

# Sample-data#sample02.ans#sample01.ans#sample01.in#sample03.in#sample03.ans#sample02.in

(N,M) = map(int, sys.stdin.readline().strip().split(" "))

roll_values = dict()
max_sum = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        key = i+j
        if not key in roll_values:
            roll_values[key] = 0
        roll_values[key] = roll_values[key]+1

        if roll_values[key] > max_sum:
            max_sum = roll_values[key]

for k in roll_values.keys():
    if roll_values[k] == max_sum:
        print(k)
