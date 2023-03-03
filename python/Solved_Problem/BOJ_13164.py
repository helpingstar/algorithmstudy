import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))

    diffs = []
    for i in range(n-1):
        diffs.append(nums[i+1] - nums[i])

    diffs.sort()

    for _ in range(k-1):
        diffs.pop()

    return sum(diffs)


print(solution())
