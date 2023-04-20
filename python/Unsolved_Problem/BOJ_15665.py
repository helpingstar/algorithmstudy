import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = set(nums)
nums = list(nums)
nums = nums * M

ans = set()

for perm in permutations(nums, M):
    ans.add(perm)

for perm in sorted(list(ans)):
    print(*perm)
