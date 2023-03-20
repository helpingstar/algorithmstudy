import sys
import bisect

input = sys.stdin.readline


def solution():
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    dp = []

    for num in nums:
        pos = bisect.bisect_left(dp, num)
        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num

    return N - len(dp)


print(solution())
