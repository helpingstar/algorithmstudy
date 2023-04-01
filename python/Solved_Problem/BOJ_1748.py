import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
result = 0

while n >= (9 * (10 ** cnt)):
    n -= (9 * (10 ** cnt))
    result += ((9 * (cnt+1)) * (10 ** cnt))
    cnt += 1

result += (cnt+1) * n

print(result)
