import sys
import bisect
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = []

for num in nums:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))