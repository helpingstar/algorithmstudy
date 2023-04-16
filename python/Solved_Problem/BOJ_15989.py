import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

n_max = max(max(nums), 3)

dp = [[0, 0, 0, 0] for _ in range(n_max+1)]

dp[1][1], dp[2][1], dp[2][2], dp[3][1], dp[3][3] = 1, 1, 1, 2, 1

for i in range(4, n_max+1):
    dp[i][1] = sum(dp[i-1])
    dp[i][2] = sum(dp[i-2][2:])
    dp[i][3] = dp[i-3][3]

for num in nums:
    print(sum(dp[num]))
