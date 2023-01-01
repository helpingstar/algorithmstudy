import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 1:
        return 'A'
    if n == 2:
        if nums[0] == nums[1]:
            return nums[0]
        else:
            return 'A'

    x = nums[1] - nums[0]
    y = nums[2] - nums[1]

    if x == 0:
        if y == 0:
            a, b = 1, 0
        else:
            return 'B'
    else:
        a = y // x
        b = nums[1] - a * nums[0]

    for i in range(n-1):
        if nums[i+1] != nums[i] * a + b:
            return 'B'
    return nums[n-1] * a + b

print(solution())
