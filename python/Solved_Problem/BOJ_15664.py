import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
check = set()
nums = list(map(int, input().split()))
nums.sort()
for comb in combinations(nums, m):
    if comb in check:
        continue
    print(*comb)
    check.add(comb)
