import sys

input = sys.stdin.readline

n = int(input())

if n < 4:
    print(n)
else:
    first, second = 2, 3
    for i in range(4, n+1):
        temp = (first + second) % 15746
        first, second = second, temp
    print(temp)
