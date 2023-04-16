import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
dp = nums[:]

ans = 0
for i, num in enumerate(nums):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], num + dp[j])
    ans = max(ans, dp[i])

# print(dp)

print(ans)
