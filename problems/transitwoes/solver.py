import sys
# Solution for Kattis problem transitwoes
# Problem url: https://open.kattis.com/problems/transitwoes

# Sample-data#transitwoes-01.ans#transitwoes-02.ans#transitwoes-02.in#transitwoes-01.in

s,t,n = map(int, sys.stdin.readline().strip().split(" "))

def readToIntList():
    return list(map(int, sys.stdin.readline().strip().split(" ")))

ds = readToIntList()
bs = readToIntList()
cs = readToIntList()

# print((s,t,n))
# print()

# print(ds)
# print()
# print(bs)
# print()
# print(cs)

# s leave home
# t class begins
# n trasit routes
# d walk time
# b rides bus time
# walking i+1 bus
# c_i bus arrives a interval

travelTime = 0
travelTime += sum(ds)
travelTime += sum(bs)
travelTime += sum(cs)
# for i in range(n):
#     travelTime += ds[i]
#     travelTime += bs[i]
#     travelTime += s[i]

result = "yes" if travelTime <= t else "no"

print(travelTime)
print(result)