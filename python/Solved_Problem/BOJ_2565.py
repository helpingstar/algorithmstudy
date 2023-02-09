import sys
import bisect

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])

nums.sort(key=lambda x: x[0])

dp = []

for i in range(n):
    pos = bisect.bisect_left(dp, nums[i][1])
    if pos == len(dp):
        dp.append(nums[i][1])
    else:
        dp[pos] = nums[i][1]

print(n - len(dp))
