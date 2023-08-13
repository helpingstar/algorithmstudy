import sys

input = sys.stdin.readline

def solution():
    N, C = map(int, input().split())
    nums = dict()
    rank = dict()
    numbers = list(map(int, input().split()))
    for i, n in enumerate(numbers):
        if n not in nums:
            nums[n] = 0
        nums[n] += 1
        if n not in rank:
            rank[n] = i

    n_list = list(nums.keys())
    n_list.sort(key=lambda x: (-nums[x], rank[x]))
    for n in n_list:
        for _ in range(nums[n]):
            print(n, end=' ')

solution()
