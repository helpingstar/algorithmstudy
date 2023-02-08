import sys
import bisect
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = []

for i in range(n):
    pos = bisect.bisect_left(dp, nums[i])
    if pos == len(dp):
        dp.append(nums[i])
    else:
        dp[pos] = nums[i]

print(n - len(dp))
