import sys
import bisect
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = []
ans = []
for i, num in enumerate(nums):
    pos = bisect.bisect_left(dp, (num, i+1))
    # print(num, pos, dp)
    if pos == len(dp):
        ans.append(0)
        dp = [(num, i+1)]
    else:
        ans.append(dp[pos][1])
        dp = [(num, i+1)] + dp[pos:]

print(*ans)
