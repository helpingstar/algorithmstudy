import sys

input = sys.stdin.readline

T = int(input())

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = max(b, a-b), min(b, a-b)

    return b

for _ in range(T):
    a, b = map(int ,input().split())
    temp = gcd(a, b)
    print(a // temp * b)
