import sys
# Solution for Kattis problem heartrate
# Problem url: https://open.kattis.com/problems/heartrate

# Sample-data#heartrate-01.in#heartrate-01.ans

n = sys.stdin.readline()

for line in sys.stdin.readlines():
    (B,P) = line.split(" ")
    (b,p) = (int(B), float(P))

    bpm = (60*b)/p
    min_abpm = bpm-bpm/b
    max_abpm = bpm+bpm/b
    print(f"{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}")