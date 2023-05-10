import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    print(f'Class {i+1}')
    nums = list(map(int, input().split()))
    L = nums[0]
    nums = nums[1:]
    nums.sort(reverse=True)

    gap = 0

    for i in range(L-1):
        gap = max(gap, nums[i]-nums[i+1])

    print(f'Max {nums[0]}, Min {nums[-1]}, Largest gap {gap}')
