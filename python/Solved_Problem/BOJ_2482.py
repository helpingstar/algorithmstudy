import sys

input = sys.stdin.readline


def solution():
    CONST = 1000000003
    N = int(input())
    K = int(input())
    prev = [i for i in range(N + 1)]
    prev[1] = 0

    for i in range(1, K):
        now = [0] * (N + 1)
        for j in range(i * 2, N + 1):
            now[j] = (now[j-1] + prev[j-2]) % CONST
        prev = now
    print(prev[-1])

solution()
