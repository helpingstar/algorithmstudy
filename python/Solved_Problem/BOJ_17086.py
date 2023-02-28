import sys
from collections import deque
input = sys.stdin.readline
INF = 1000
R, C = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]
distance = [[INF] * C for _ in range(R)]

def bfs(x, y, dist):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < R and 0 <= ny < C):
                    continue
                if dist[nx][ny] <= dist[x][y] + 1:
                    continue
                if board[nx][ny] == 1:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            bfs(r, c, distance)

for r in range(R):
    for c in range(C):
        ans = max(ans, distance[r][c])

print(ans)
