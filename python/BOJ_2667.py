import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))
    
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if matrix[x][y] == 0:
        return False
    count = 1
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        matrix[a][b] = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if matrix[nx][ny] == 0:
                continue
            matrix[nx][ny] = 0
            count += 1
            queue.append((nx, ny))
    return count

house_list = []

for i in range(n):
    for j in range(n):
        result = bfs(i, j)
        if result:
            house_list.append(result)
            
house_list.sort()

print(len(house_list))
for house in house_list:
    print(house)