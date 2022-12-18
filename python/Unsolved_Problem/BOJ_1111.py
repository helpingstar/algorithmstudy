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
        # elif nums[0] == 0:        # 0, 4는 -> a: n, b:4 가능하므로 'A'
        #     return nums[1] * 2
        else:
            return 'A'

    x = nums[1] - nums[0]
    y = nums[2] - nums[1]

    if x == 0 or y == 0:
        if x == 0 and y == 0:
            a = 1
            b = 0
        else:
            if y == 0:
                a = 0
                b = nums[1]
            else:
                return 'B'
    else:
        a = y // x
        b = nums[1] - (nums[0] * a)

    for i in range(len(nums)-1):
        if nums[i] * a + b != nums[i+1]:
            return 'B'
    return nums[len(nums) - 1] *a + b

print(solution())
