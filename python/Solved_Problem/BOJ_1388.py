import sys
from collections import deque

input = sys.stdin.readline

height, width = map(int, input().split())

board = []
visited = []

delta = [-1, 1]

for _ in range(height):
    line = input().rstrip()
    board.append(line)
    visited.append([False] * width)

def bfs_hor(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d_y in delta:
            ny = y + d_y

            if not (0 <= ny < width):
                continue
            if visited[x][ny]:
                continue

            if board[x][ny] == '-':
                q.append((x, ny))
                visited[x][ny] = True

def bfs_ver(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d_x in delta:
            nx = x + d_x

            if not (0 <= nx < height):
                continue
            if visited[nx][y]:
                continue

            if board[nx][y] == '|':
                q.append((nx, y))
                visited[nx][y] = True

count = 0
for r in range(height):
    for c in range(width):
        if not visited[r][c]:
            if board[r][c] == '-':
                bfs_hor(r, c)
            else:
                bfs_ver(r, c)
            count += 1
print(count)
