import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int ,input().split())
    result = 1
    for i in range(b, b-a, -1):
        result *= i
    for i in range(1, a+1):
        result //= i
    print(result)
