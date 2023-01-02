import sys
import bisect

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = []
cp = [0] * n

for i, num in enumerate(nums):
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num
    cp[i] = pos

print(len(dp))

cur = len(dp) - 1
ans = []

for i in range(n-1, -1, -1):
    if cp[i] == cur:
        cur -= 1
        ans.append(nums[i])


print(*ans[::-1])
