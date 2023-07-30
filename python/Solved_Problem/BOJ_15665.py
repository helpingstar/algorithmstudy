import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    nums = sorted(list(set(map(int, input().split()))))

    def dp(idx, numbers):
        nonlocal M, nums
        if idx == M:
            print(*numbers)
            return
        for i in nums:
            dp(idx+1, numbers+[i])

    dp(0, [])


solution()
