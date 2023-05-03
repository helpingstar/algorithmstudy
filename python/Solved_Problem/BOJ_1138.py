import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

target = list(map(int, input().split()))

for perm in permutations(range(1, N+1), N):
    table = [0] * (N)
    result = [0] * (N)
    for p in perm:
        # print(p)
        result[p-1] = table[p-1]
        for i in range(p-1):
            table[i] += 1

    if result == target:
        print(*perm)
        break
