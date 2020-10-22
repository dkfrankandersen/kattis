import sys

# Solution for Kattis problem provincesandgold
# Problem url: https://open.kattis.com/problems/provincesandgold

# Sample-data files
# sample01.ans
# sample01.in
# sample02.ans
# sample02.in
# sample03.ans
# sample03.in

G,S,C = map(int, sys.stdin.readline().split(" "))


# 3 kinds of victory cards
# Province (costs 8, worth 6 victory points)
# Duchy (costs 5, worth 3 victory points)
# Estate (costs 2, worth 1 victory point)

# 3 kinds of treasure cards
# Gold (costs 6, worth 3 buying power)
# Silver (costs 3, worth 2 buying power)
# Copper (costs 0, worth 1 buying power)

result = ""
buyingPower = G*3+S*2+1*C
if buyingPower >= 8:
    result += "Province or "
elif buyingPower >= 5:
    result += "Duchy or "
elif buyingPower >= 2:
    result += "Estate or "

if buyingPower >= 6:
    result += "Gold"
elif buyingPower >= 3:
    result += "Silver"
else:
    result += "Copper"

print(result)
