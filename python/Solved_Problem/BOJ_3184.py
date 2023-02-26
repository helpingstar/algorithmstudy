import sys
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

result_sheep, result_wolf = 0, 0

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    n_sheep, n_wolf = 0, 0
    if board[x][y] == 'o':
        n_sheep += 1
    if board[x][y] == 'v':
        n_wolf += 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == '#':
                continue
            
            if board[nx][ny] == 'o':
                n_sheep += 1
            if board[nx][ny] == 'v':
                n_wolf += 1
            
            visited[nx][ny] = True
            q.append((nx, ny))
    # print(n_sheep, n_wolf)
    if n_sheep > n_wolf:
        return (n_sheep, 0)
    else:
        return (0, n_wolf)      

for r in range(R):
    for c in range(C):
        if not visited[r][c]:
            temp_sheep, temp_wolf = bfs(r, c)
            result_sheep += temp_sheep
            result_wolf += temp_wolf

print(result_sheep, result_wolf)