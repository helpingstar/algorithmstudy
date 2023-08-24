import sys

def solution():
    input = sys.stdin.readline

    N = int(input())
    check = [False] * 2_000_001

    for _ in range(N):
        check[int(input()) + 1_000_000] = True

    for i in range(2_000_000, -1, -1):
        if check[i]:
            print(i - 1_000_000)

solution()
