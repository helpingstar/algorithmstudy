import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

island = [[0] * n for _ in range(n)]
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cordis = []
bridge_length = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs_island(y, x, visited, island_cnt):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if arr[ny][nx] == 1:
                cordis.append((ny, nx, island_cnt)) 
                island[ny][nx] = island_cnt
                q.append((ny, nx))
            

def find_island():
    visited = [[False for _ in range(n)] for _ in range(n)]
    island_cnt = 1
    # i : row, j : column
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                cordis.append((i, j, island_cnt))
                island[i][j] = island_cnt
                bfs_island(i, j, visited, island_cnt)
                island_cnt += 1
    return island_cnt

def bfs_bridge(sy, sx, cnt):
    q = deque()
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        visited = [[False] * n for _ in range(n)]
        visited[y][x] = True
        table = [[0] * n for _ in range(n)]
        for i in range(4):
            ny = y + dy[i]
            nx = x = dx[i]

            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if island[ny][nx] == 0:
                table[ny][nx] = table[y][x] + 1
                q.append((ny, nx))
            elif island[ny][nx] != cnt:
                return table[y][x]
                
def find_bridge():
    for sy, sx, cnt in cordis:
        bridge_length.append(bfs_bridge(sy, sx, cnt))


island_num = find_island() - 1
find_bridge()
print(min(bridge_length))