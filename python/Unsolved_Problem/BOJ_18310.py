import sys
import math

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

nums.sort()

min_dist = float('inf')
ans = 0

for i in range(nums[0], nums[-1] + 1):
    temp = 0
    for num in nums:
        temp += abs(num - i)

    if temp < min_dist:
        ans = i
        min_dist = temp

print(ans)
