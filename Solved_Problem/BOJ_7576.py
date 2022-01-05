import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

matrix = []
start_tomato = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tomato_line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if tomato_line[j] == 1:
            start_tomato.append((i, j))
    matrix.append(tomato_line)
    
def bfs(tomato_list):
    queue = deque(tomato_list)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            matrix[nx][ny] = matrix[x][y] + 1

def for_return(matrix):
    max = 0
    for line in matrix:
        for c in line:
            if c == 0:
                return -1
            if max < c:
                max = c
    return max - 1

bfs(start_tomato)
print(for_return(matrix))