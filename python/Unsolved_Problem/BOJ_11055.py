import sys
import bisect

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [0]
sum_dp = [0]

for num in nums:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
        sum_dp.append(sum_dp[-1] + num)
    else:
        dp[pos] = num
        sum_dp[pos] = max(sum_dp[pos], sum_dp[pos-1] + num)

print(dp)
print(sum_dp)
print(max(sum_dp))
