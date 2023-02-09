import sys

input = sys.stdin.readline

T = int(input())

def solution():
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if x % n == (y % n):
            return x
        x += m
    return -1


for _ in range(T):
    print(solution())
