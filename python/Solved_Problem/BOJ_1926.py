import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = [list(map(int, input().split())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1
    return cnt

max_ans = 0
ans = 0

for r in range(R):
    for c in range(C):
        if not visited[r][c] and board[r][c] == 1:
            max_ans = max(max_ans, bfs(r, c))
            ans += 1

print(ans)
print(max_ans)
