import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if board[nx][ny] == 'R':
                continue
            
            

for r in range(R):
    for c in range(C):
        