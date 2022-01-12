import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
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
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] == 0:
                continue
            matrix[nx][ny] = 0
            count += 1
            queue.append((nx, ny))
    return count

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    matrix = []
    one_list = []
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(n):
        matrix.append([0] * m)
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        one_list.append((x, y))
        matrix[x][y] = 1
    queue = deque()
    count = 0
    for one in one_list:
        if bfs(one[0], one[1]):
            count += 1
    print(count)
