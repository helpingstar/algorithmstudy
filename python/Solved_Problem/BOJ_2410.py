import sys

input = sys.stdin.readline
MOD = 1000000000
n = int(input())

dp = [0] * (n+1)
dp[0] = 1

cur = 0
while (1 << cur) <= n:
    temp = 1 << cur
    for i in range(temp, n+1):
        dp[i] += dp[i-temp]
        dp[i] %= MOD
    cur += 1

print(dp[n])
