import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
nums = []
for _ in range(n):
    temp = int(input())
    nums.append(temp)
    dp[temp] = 1

nums.sort()

for i in range(k+1):
    for n in nums:
        if i + n <= k:
            dp[i+n] += 1
print(dp)
print(dp[k])
