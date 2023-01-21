import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = [list(input().rstrip()) for _ in range(n)]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

def bfs(x, y, rg, visited):
    if board[x][y] == 'B':
        color = {'B'}
    else:
        if rg:
            color = {'R', 'G'}
        else:
            if board[x][y] == 'R':
                color = {'R'}
            else:
                color = {'G'}
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] not in color:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

result1 = 0
for r in range(n):
    for c in range(n):
        if not visited1[r][c]:
            bfs(r, c, False, visited1)
            result1 += 1

result2 = 0
for r in range(n):
    for c in range(n):
        if not visited2[r][c]:
            bfs(r, c, True, visited2)
            result2 += 1

print(result1, result2)
