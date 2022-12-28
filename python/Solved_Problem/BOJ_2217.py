import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort()

ans = 0

for i, num in enumerate(nums):
    ans = max(ans, num*(n-i))

print(ans)
