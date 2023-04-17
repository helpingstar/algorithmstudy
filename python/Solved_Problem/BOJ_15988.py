import sys

input = sys.stdin.readline

MOD = 1000000009

N = int(input())

nums = [int(input()) for _ in range(N)]

s_nums = set(nums)

answer_map = {1: 1, 2: 2, 3: 4}

n_max = max(nums)

dp = [0] * 3

dp[0], dp[1], dp[2] = 4, 1, 2

for i in range(4, n_max+1):
    dp[i % 3] = sum(dp) % MOD
    if i in s_nums:
        answer_map[i] = dp[i % 3]

for num in nums:
    print(answer_map[num])
