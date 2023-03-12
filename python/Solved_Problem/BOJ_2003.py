import sys

input = sys.stdin.readline

n, target = map(int, input().split())

nums = list(map(int, input().split()))

sums = [0]

for i in range(n):
    sums.append(sums[i]+nums[i])
ans = 0

l, r = 0, 0

while l <= r and r <= n:
    temp = sums[r] - sums[l]
    if temp < target:
        r += 1
    elif temp > target:
        l += 1
    else:
        ans += 1
        r += 1
        l += 1

print(ans)
