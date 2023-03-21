import sys
import bisect

N = int(input())

dp = []
nums = list(map(int, input().split()))

for num in nums:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))
