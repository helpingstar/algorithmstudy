import sys
from itertools import combinations

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))
    
    if n == 1:
        return 0
    if k == 1:
        return nums[-1] - nums[0]
    ans = sys.maxsize
    for combis in combinations(range(1, n), k-1):
        result = 0
        result += (nums[combis[0]-1] - nums[0])
        result += (nums[-1] - nums[combis[-1]])

        for i in range(k-2):
            result += (nums[combis[i+1]-1] - nums[combis[i]])
        ans = min(result, ans)

    return ans

print(solution())