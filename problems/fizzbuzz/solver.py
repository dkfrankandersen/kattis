import sys
# Solution for Kattis problem fizzbuzz
# Problem url: https://open.kattis.com/problems/fizzbuzz

# Sample-data#fizzbuzz-01.in#fizzbuzz-01.ans#fizzbuzz-02.in#fizzbuzz-02.ans#fizzbuzz-03.in#fizzbuzz-03.ans

(X, Y, N) = sys.stdin.readline().split(" ")
(X, Y, N) = tuple(map(int, (X, Y, N)))

for i in range(1, N+1):
    if (i % X == 0 and i % Y== 0):
        print("FizzBuzz")
    elif(i % X == 0):
            print("Fizz")
    elif(i % Y== 0):
        print("Buzz")
    else:
        print(i)



