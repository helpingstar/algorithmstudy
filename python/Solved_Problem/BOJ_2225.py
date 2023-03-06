import sys

input = sys.stdin.readline

n, k = map(int, input().split())
MOD = 1000000000
prev_dp = [0] * (n+1)
prev_dp[0] = 1

for _ in range(k):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = (prev_dp[i] + dp[i-1]) % MOD
    # print(dp)
    prev_dp = dp

print(dp[n])
