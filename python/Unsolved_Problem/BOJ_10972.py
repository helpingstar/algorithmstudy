import sys
from itertools import permutations


def solution():
    input = sys.stdin.readline

    N = int(input())
    nums = tuple(map(int, input().split()))
    flag = False
    for perm in permutations(range(1, N+1), N):
        if flag:
            print(*perm)
            return
        if perm == nums:
            flag = True
    print(-1)


solution()
