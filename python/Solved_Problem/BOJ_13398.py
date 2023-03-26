import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = [0] * N
dp0 = [0] * N

has_zero = False
answer = 0

minus_max = -float('inf')

for i in range(N):
    if nums[i] == 0:
        has_zero = True
    if nums[i] < 0:
        minus_max = max(minus_max, nums[i])

    dp[i] = max(dp[i], dp[i-1] + nums[i])
    dp0[i] = max(dp0[i-1]+nums[i], dp[i-1])

    answer = max(answer, dp[i], dp0[i])

if not has_zero and answer == 0:
    print(minus_max)
else:
    print(answer)
