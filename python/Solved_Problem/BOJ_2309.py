import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

target = sum(nums) - 100

nums.sort()

l, r = 0, 8

while l < r:
    if nums[l] + nums[r] == target:
        break
    elif nums[l] + nums[r] > target:
        r -= 1
    else:
        l += 1

for i in range(9):
    if i == l or i == r:
        continue
    print(nums[i])
