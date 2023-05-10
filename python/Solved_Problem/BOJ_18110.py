import sys
import math

input = sys.stdin.readline


def round(num):
    if num - math.floor(num) >= 0.5:
        return math.floor(num) + 1
    else:
        return math.floor(num)


def solution():
    T = int(input())

    if T == 0:
        return 0

    nums = [int(input()) for _ in range(T)]

    nums.sort()

    cut = int(round(T * 0.15))

    # print(f'cut : {cut}')

    # print(nums)
    # print(f'nums[cut:T-cut]: {nums[cut:T-cut]}')
    return int(round(sum(nums[cut:T-cut]) / (T - 2 * cut)))


print(solution())
