import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

nums.sort(reverse=True)
ans = 0

for i, num in enumerate(nums, 2):
    ans = max(ans, i + num)

print(ans)
