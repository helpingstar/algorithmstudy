import sys
from collections import deque

input = sys.stdin.readline

R, C, K = map(int, input().split())

board = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(x, y):
    visited[x][y] = True
    size = 1

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if board[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny))
            size += 1
            visited[nx][ny] = True

    return size

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

ans = 0

for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            ans = max(ans, bfs(r, c))

print(ans)
