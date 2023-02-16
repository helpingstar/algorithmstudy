import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1

for i in range(n+1):
    for j in range(1, n+1):
        if 0 <= i - j:
            dp[i] += dp[i-j]

print(dp)
print(dp[-1])