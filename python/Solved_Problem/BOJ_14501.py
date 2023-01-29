import sys

input = sys.stdin.readline

times = []
pays = []

n = int(input())
ans = 0
dp = [0] * (n+1)
now = 0
for i in range(n):
    time, pay = map(int, input().split())
    # times.append(time)
    # pays.append(pay)
    now = max(dp[i], now)
    if i + time <= n:
        dp[i+time] = max(dp[i+time], now + pay)
        ans = max(ans, dp[i+time])

print(ans)
