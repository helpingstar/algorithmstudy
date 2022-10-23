import sys
import bisect

input = sys.stdin.readline

n = int(input())

arr = list(map(int ,input().split()))

dp = [1001] * (n + 1)
dp[0] = arr[0]
max_n = 0

for i in arr[1:]:
    temp = bisect.bisect_left(dp, i)
    dp[temp] = i
    max_n = max(max_n, temp)

print(max_n + 1)
