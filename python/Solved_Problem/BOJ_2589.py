import sys

input = sys.stdin.readline
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

def bfs(x, y):
    visited = set()
    visited.add((x, y))
    q = deque()
    q.append((x, y, 0))

    while q:
        x, y, step = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if (nx, ny) in visited:
                continue
            if board[nx][ny] == 'W':
                continue
            q.append((nx, ny, step+1))
            visited.add((nx, ny))
    return step
ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == 'L':
            ans = max(ans, bfs(r, c))

print(ans)
