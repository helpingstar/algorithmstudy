import sys


def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    nums = list(set(nums))

    if M == 0:
        return 0

    nums.sort()

    l, r = 0, 1
    result = float("inf")
    while l <= r and r < len(nums):
        temp = nums[r] - nums[l]
        if temp == M:
            return M
        elif temp > M:
            l += 1
            result = min(temp, result)
        else:
            r += 1
    return result


print(solution())

"""
7 4
1
8
15
16
17
18
22
"""
