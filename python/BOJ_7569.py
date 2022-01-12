import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

box = []
tomato = 0
old_tomato_pos = deque()
for v in range(h):
    matrix = []
    for x in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for y in range(m):
            if line[y] == 0:
                tomato += 1
            elif line[y] == 1:
                old_tomato_pos.append((v, x, y))
        matrix.append(line)
        
    box.append(matrix)

dv = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

def bfs(tomato):
    max = 0
    while old_tomato_pos:
        v, x, y = old_tomato_pos.popleft()
        for i in range(6):
            nv = v + dv[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nx < n and 0 <= ny < m and 0 <= nv <h):
                continue
            if box[nv][nx][ny] != 0:
                continue
            
            old_tomato_pos.append((nv, nx, ny))
            box[nv][nx][ny] = box[v][x][y] + 1
            if box[nv][nx][ny] > max:
                max = box[nv][nx][ny]
            tomato -= 1
            if tomato == 0:
                return max - 1
    return -1

if tomato == m * n * h:
    print(-1)
elif tomato == 0:
    print(0)
else:
    print(bfs(tomato))