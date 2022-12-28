import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_row, n_col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n_row)]
indegree = [[0] * n_col for _ in range(n_row)]
road = [[0] * n_col for _ in range(n_row)]
way = [[[] for _ in range(n_col)] for _ in range(n_row)]
road[0][0] = 1

for r in range(n_row):
    for c in range(n_col):
        if r > 0 and board[r-1][c] < board[r][c]:
            indegree[r-1][c] += 1  # up
            way[r][c].append((-1, 0))
        if r < n_row - 1 and board[r+1][c] < board[r][c]:
            indegree[r+1][c] += 1  # down
            way[r][c].append((1, 0))
        if c > 0 and board[r][c-1] < board[r][c]:
            indegree[r][c-1] += 1  # left
            way[r][c].append((0, -1))
        if c < n_col - 1 and board[r][c+1] < board[r][c]:
            indegree[r][c+1] += 1  # right
            way[r][c].append((0, 1))

q = deque()

for r in range(n_row):
    for c in range(n_col):
        if indegree[r][c] == 0:
            q.append((r, c))

while q:
    x, y = q.popleft()
    for dx, dy in way[x][y]:
        nx = x + dx
        ny = y + dy
        indegree[nx][ny] -= 1
        road[nx][ny] += road[x][y]
        if indegree[nx][ny] == 0:
            q.append((nx, ny))

print(road[-1][-1])
