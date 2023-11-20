import sys
from itertools import permutations

input = sys.stdin.readline

def solution():
    N = int(input())
    K = int(input())

    nums = [input().rstrip() for _ in range(N)]
    result = set()
    for perm in permutations(range(N), K):
        temp = ''
        for i in perm:
            temp += nums[i]
        result.add(int(temp))
    
    print(len(result))

solution()