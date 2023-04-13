import copy
import sys
from itertools import permutations
input = sys.stdin.readline

R, C, n_spin = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

spins = [tuple(map(int, input().split())) for _ in range(n_spin)]
ans = sys.maxsize

for perm in permutations(spins, n_spin):
    temp = copy.deepcopy(board)
    for r, c, length_s in perm:
        r -= 1
        c -= 1
        for s in range(1, length_s+1):
            one = temp[r-s][c+s]
            temp[r-s][c-s+1:c+s+1] = temp[r-s][c-s:c+s]
            for i in range(r-s, r+s):
                temp[i][c-s] = temp[i+1][c-s]
            temp[r+s][c-s:c+s] = temp[r+s][c-s+1:c+s+1]
            for i in range(r+s, r-s, -1):
                temp[i][c+s] = temp[i-1][c+s]
            temp[r-s+1][c+s] = one

    for line in temp:
        ans = min(ans, sum(line))


print(ans)
