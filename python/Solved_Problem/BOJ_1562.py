import sys

input = sys.stdin.readline

n = int(input())

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(1, n):
    for now in range(10):
        for bit in range(1024):
            if now < 9:
                next_bit = bit | 1 << (now+1)
                dp[i+1][now+1][next_bit] += dp[i][now][bit]
                dp[i+1][now+1][next_bit] %= 1000000000
            if now > 0:
                next_bit = bit | 1 << (now-1)
                dp[i+1][now-1][next_bit] += dp[i][now][bit]
                dp[i+1][now-1][next_bit] %= 1000000000

ans = 0
for i in range(10):
    ans += dp[n][i][1023]

print(ans % 1000000000)
