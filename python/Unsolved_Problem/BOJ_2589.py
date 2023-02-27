import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
distance1 = [[0] * C for _ in range(R)]
distance2 = [[0] * C for _ in range(R)]

def bfs(x, y, distance):
    distance[x][y] = 1
    q = deque()
    q.append((x, y))
    max_dist = 1
    rx, ry = -1, -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if distance[nx][ny] > 0:
                continue
            if board[nx][ny] == 'W':
                continue

            distance[nx][ny] = distance[x][y] + 1
            if distance[x][y] + 1 > max_dist:
                max_dist = distance[x][y] + 1
                rx, ry = nx, ny
            q.append((nx, ny))

    return (rx, ry, max_dist)

ans = 0

for r in range(R):
    for c in range(C):
        if board[r][c] == 'L':
            if distance1[r][c] == 0:
                x, y, _ = bfs(r, c, distance1)
                _, _, dist = bfs(x, y, distance2)
                ans = max(dist, ans)

# for i in distance1:
#     print(i)
# print('-'*10)
# for i in distance2:
#     print(i)
print(ans-1)
