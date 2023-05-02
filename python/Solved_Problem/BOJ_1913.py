import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
target = int(input())

board = [[-1] * N for _ in range(N)]

board[N//2][N//2] = 1

q = deque()

# 0: right / 1: down / 2: left / 3: up

def nxt_pos(x, y, way):
    if way == 0:
        return x, y+1
    elif way == 1:
        return x+1, y
    elif way == 2:
        return x, y-1
    else:
        return x-1, y

def nxt_way(x, y, way):
    if x + y == N-1:
        if x < N//2:
            return 1
        else:
            return 3
    elif x == y and x > N//2:
        return 2
    elif x + 1 == y and x < N//2:
        return 0

    return way

x, y = N//2 - 1, N//2
ax, ay = N//2, N//2
way = 0
for i in range(2, N*N+1):
    board[x][y] = i
    if i == target:
        ax, ay = x, y
    nx, ny = nxt_pos(x, y, way)
    nway = nxt_way(nx, ny, way)


    x, y, way = nx, ny, nway

for line in board:
    print(*line)
print(ax+1, ay+1)
