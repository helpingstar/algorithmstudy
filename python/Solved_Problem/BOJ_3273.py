import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.sort()
target = int(input())

l, r = 0, n-1
ans = 0
while l < r:
    if nums[l] + nums[r] == target:
        l += 1
        r -= 1
        ans += 1
    elif nums[l] + nums[r] < target:
        l += 1
    else:
        r -= 1

print(ans)
