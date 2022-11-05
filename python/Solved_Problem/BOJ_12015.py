import sys
import bisect
INF = sys.maxsize

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [INF] * (n+1)
dp[0] = 0
ans = 0
for num in arr:
    pos = bisect.bisect_left(dp, num)
    ans = max(ans, pos)
    dp[pos] = num

print(ans)
