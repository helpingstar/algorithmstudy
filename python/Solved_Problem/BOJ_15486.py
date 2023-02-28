import sys
from collections import deque
input = sys.stdin.readline

times = []
prices = []

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    times.append(a)
    prices.append(b)

dp = [0] * (n+1)

for i in range(n):
    if i + times[i] <= n:
        dp[i + times[i]] = max(dp[i + times[i]], dp[i] + prices[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])
