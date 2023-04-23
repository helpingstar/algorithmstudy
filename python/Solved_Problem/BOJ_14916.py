import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    if N in {1, 3}:
        return -1
    quo, remainder = N // 5, N % 5

    ans = 0
    if remainder == 1:
        return quo + 2
    elif remainder == 2:
        return quo + 1
    elif remainder == 3:
        return quo + 3
    elif remainder == 4:
        return quo + 2
    else:
        return quo


print(solution())
