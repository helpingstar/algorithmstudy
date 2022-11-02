import sys

input = sys.stdin.readline
INF = sys.maxsize
t = int(input())
ab_list = []
max_diff = 0
for _ in range(t):
    a, b = map(int, input().split())
    ab_list.append((a, b))
    max_diff = max(max_diff, b-a)

dp = [INF] * (max_diff+1)
dp[0], dp[1] = 0, 1
for i in range(1, max_diff+1):
    now = dp[i]
    if i + now - 1 < max_diff:
        dp[i + now-1] = min(dp[i + now-1], now + 1)
    if i + now < max_diff:
        dp[i + now]   = min(dp[i + now], now + 1)
    if i + now + 1 < max_diff:
        dp[i + now+1] = min(dp[i + now+1], now + 1)

for a, b in ab_list:
    print(dp[b-a])