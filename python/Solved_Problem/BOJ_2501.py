import sys

input = sys.stdin.readline

def solution():
    n, k = map(int ,input().split())
    for i in range(1, n+1):
        if n % i == 0:
            k -= 1
        if k == 0:
            return i
    return 0

print(solution())
