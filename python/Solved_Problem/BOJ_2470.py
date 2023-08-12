import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    if nums[-2] == 0 or nums[-1] < 0:
        print(nums[-2], nums[-1])
        return

    if nums[1] == 0 or nums[0] > 0:
        print(nums[0], nums[1])
        return

    if nums[0] == 0:
        print(0, nums[1])
        return

    if nums[-1] == 0:
        print(nums[-2], 0)
        return

    l, r = 0, N-1
    result = float('inf')
    la = -1
    ra = -1
    while l < r:
        sum_ = nums[l] + nums[r]
        if abs(sum_) < result:
            result = abs(sum_)
            la = l
            ra = r
        if sum_ < 0:
            l += 1
        elif sum_ > 0:
            r -= 1
        else:
            print(nums[l], nums[r])
            return
    print(nums[la], nums[ra])
    return


solution()
