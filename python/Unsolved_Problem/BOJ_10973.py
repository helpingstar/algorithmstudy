import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

target = tuple(map(int, input().split()))

if target == tuple(range(1, N+1)):
    print(-1)
else:
    prev = tuple(range(1, N+1))
    for perm in permutations(range(1, N+1), N):
        if target == perm:
            print(*prev)
            break
        prev = perm
