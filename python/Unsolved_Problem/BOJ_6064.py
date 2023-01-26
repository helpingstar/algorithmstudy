import sys

input = sys.stdin.readline

T = int(input())

def solution(m, n, x, y):
    for i in range(1, m*n+1):
        if (i % m, i % n) == (x, y):
            return i
    return -1

for _ in range(T):
    m, n, x, y = map(int, input().split())
    print(solution(m, n, x, y))
