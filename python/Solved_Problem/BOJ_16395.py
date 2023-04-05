import sys

input = sys.stdin.readline

n, k = map(int, input().split())


result = 1

for i in range(2, n):
    result *= i

for i in range(2, k):
    result //= i

for i in range(2, n-k+1):
    result //= i

print(result)
