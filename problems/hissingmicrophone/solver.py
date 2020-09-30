import sys
import re as re
# Solution for Kattis problem hissingmicrophone
# Problem url: https://open.kattis.com/problems/hissingmicrophone

# Sample-data#hissingmicrophone-03.ans#hissingmicrophone-02.ans#hissingmicrophone-01.ans#hissingmicrophone-02.in#hissingmicrophone-03.in#hissingmicrophone-01.in

word = sys.stdin.readline().strip()
if len(re.findall('ss', word)) > 0:
    print("hiss")
else:
    print("no hiss")