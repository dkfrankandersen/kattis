from os import terminal_size
import sys
# Solution for Kattis problem nodup
# Problem url: https://open.kattis.com/problems/nodup

# Sample-data#2.ans#1.in#3.in#2.in#3.ans#1.ans
 
lst = sys.stdin.readline().strip().split(" ")
unique = set(lst)

print("yes" if len(lst) == len(unique) else "no")
