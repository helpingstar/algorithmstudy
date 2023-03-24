import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
ans = 0
for perm in permutations(nums, N):
    result = 0
    for i in range(N-1):
        result += abs(perm[i] - perm[i+1])
    ans = max(ans, result)

print(ans)
