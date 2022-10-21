import sys

input = sys.stdin.readline

n = int(input())

minus2 = 0
minus1 = 1
for _ in range(n-1):
    temp = (minus2 + minus1) % 1000000007
    minus2, minus1 = minus1, temp

print(temp)
