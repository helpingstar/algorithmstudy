import sys

input = sys.stdin.readline

N, C = map(int, input().split())

nums = list(map(int, input().split()))

idx = [-1] * (C+1)
count = [0] * (C+1)

for i, num in enumerate(nums):
    if idx[num] == -1:
        idx[num] = i

    count[num] += 1

nums = list(range(1, C+1))

nums.sort(key=lambda x: (-count[x], idx[x]))

for num in nums:
    print(f'{num} '*count[num], end='')
