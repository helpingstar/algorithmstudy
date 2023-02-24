import sys

input = sys.stdin.readline

number = input().rstrip()

length = len(number)

dp = [0] * (length + 1)
dp[0] = 1

for i in range(1, length+1):
    idx = i-1
    if 0 < int(number[idx]) <= 9:
        dp[i] += dp[i-1]
    if 2 <= i and 10 <= int(number[idx-1:idx+1]) <= 26:
        dp[i] += dp[i-2]
    dp[i] %= 1000000

# print(dp)
print(dp[length])
