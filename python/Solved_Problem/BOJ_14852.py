import sys

input = sys.stdin.readline
MOD = 1000000007


def solution():
    N = int(input())
    if N == 1:
        return 2
    elif N == 2:
        return 7
    elif N == 3:
        return 22

    nums = [0] * (N+1)
    nums[1], nums[2], nums[3] = 2, 7, 22
    sums = [0] * (N+1)
    sums[1], sums[2], sums[3] = 2, 9, 31

    for i in range(4, N+1):
        nums[i] = (nums[i-1] * 2 + nums[i-2] * 3 + 2 + sums[i-3] * 2) % MOD
        sums[i] = (sums[i-1] + nums[i]) % MOD
    return nums[N]


print(solution())
