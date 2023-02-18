import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    combis = list(combinations(nums, i))
    for comb in combis:
        if sum(comb) == s:
            ans += 1

print(ans)