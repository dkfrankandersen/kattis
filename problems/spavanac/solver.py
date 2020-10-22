import sys

# Solution for Kattis problem spavanac
# Problem url: https://open.kattis.com/problems/spavanac

# Sample-data files
# spavanac.3.ans
# spavanac.1.ans
# spavanac.1.in
# spavanac.3.in
# spavanac.2.ans
# spavanac.2.in

H, M = map(int, sys.stdin.readline().strip().split(" "))

def main():
    min = H*60+M-45
    Mn = min%60
    Hn = int(((min-Mn)/60)) % 24
    print(f"{Hn} {Mn}")

main()