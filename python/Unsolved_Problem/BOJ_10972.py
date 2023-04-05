import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
target = tuple(map(int, input().split()))

length = 1

for i in range(2, N+1):
    length *= i
flag = False
find = False
for i, comb in enumerate(permutations(range(1, N+1), N)):
    if flag:
        find = True
        break
    if comb == target:
        flag = True

if find:
    print(*comb)
else:
    print(-1)
