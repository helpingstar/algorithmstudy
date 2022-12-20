# 1562 계단수
MOD = 1000000000
n = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]
for k in range(1, 10):
    dp[1][k][1 << k] = 1

for length in range(n):
    for last in range(10):
        for bit in range(1024):
            if last < 9:
                next_bit = bit | (1 << (last + 1))
                dp[(length + 1)][last + 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last + 1][next_bit] %= MOD

            if last > 0:
                next_bit = bit | (1 << (last - 1))
                dp[(length + 1)][last - 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last - 1][next_bit] %= MOD

answer = 0
for last in range(10):
    answer += dp[n][last][1023]
    answer %= MOD

print(answer)
