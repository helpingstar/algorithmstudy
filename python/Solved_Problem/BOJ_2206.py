import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

candidate = []

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip())))
INF = int(1e10)
start_dis = [[INF] * m for _ in range(n)]
end_dis = [[INF] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, dis_matrix):
    queue = deque()
    queue.append((x, y))
    dis_matrix[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if dis_matrix[nx][ny] <= dis_matrix[x][y] + 1:
                continue
            if matrix[nx][ny] == 1:
                continue
            dis_matrix[nx][ny] = dis_matrix[x][y] + 1
            queue.append((nx, ny))

def one_bfs(x, y, dis_matrix):
    queue = deque()
    queue.append((x, y))
    dis_matrix[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if dis_matrix[nx][ny] <= dis_matrix[x][y] + 1:
                continue
            if matrix[nx][ny] == 1:
                for j in range(4):
                    one_x = nx + dx[j]
                    one_y = ny + dy[j]
                    
                    if not (0 <= one_x < n and 0 <= one_y < m):
                        continue
                    if end_dis[one_x][one_y] == INF:
                        continue
                    candidate.append(dis_matrix[x][y] + end_dis[one_x][one_y] + 1)
                continue
            dis_matrix[nx][ny] = dis_matrix[x][y] + 1
            queue.append((nx, ny))
            
bfs(n-1, m-1, end_dis)
candidate.append(end_dis[0][0])
one_bfs(0, 0, start_dis)

if min(candidate) == INF:
    print(-1)
else:
    print(min(candidate))