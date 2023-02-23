import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for num in nums:
    for i in range(num, k+1):
        dp[i] += dp[i - num]

print(dp[k])