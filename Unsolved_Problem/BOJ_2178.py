import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(n, m):
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1
    return matrix[n-1][m-1]

print(bfs(n, m))