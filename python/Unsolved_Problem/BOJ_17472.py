import sys
from collections import deque

input = sys.stdin.readline

# r : 세로 길이, c : 가로 길이
r, c = map(int, input().split())

islands = [[0 for _ in range(c)] for _ in range(r)]
arr = [list(map(int, input().split())) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
edges = []
cordis = []

# 방문하지 않은 island안에 들어가서 island의 각 위치를 파악하고
# 각 위치를 이름으로 넘버링 한다.
def bfs_islands(visited, sy, sx, island_num):

    q = deque()
    q.append((sy, sx))
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < r and 0 <= nx < c):
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if arr[ny][nx] == 1:
                islands[ny][nx] = island_num
                q.append((ny, nx))
                cordis.append((ny, nx, island_num))
                

# islands 의 존재를 찾는 함수
def make_islands():
    visited = [[False for _ in range(c)] for _ in range(r)]
    # island의 이름
    island_num = 1
    # 행 탐색
    for i in range(r):
        # 열 탐색
        for j in range(c):
            # 방문하지 않았고 그곳이 섬 지형이라면
            if not visited[i][j] and arr[i][j] == 1:
                # 방문으로 처리
                visited[i][j] = True
                # 섬에 넘버링
                islands[i][j] = island_num
                # 섬의 (x, y, island_num) : 
                cordis.append((i, j, island_num))
                bfs_islands(visited, i, j, island_num)
                island_num += 1
    return island_num

# 다리의 후보군을 찾는 함수
def find_routes():
    for sy, sx, island_num in cordis:
        q = deque()

        for i in range(4):
            q.append((sy, sx))
            visited = [[False] * c for _ in range(r)]
            visited[sy][sx] = True
            table = [[0] * c for _ in range(r)]
            
            while q:
                y, x = q.popleft()
                ny = y + dy[i]
                nx = x + dx[i]
                
                if not (0 <= ny < r and 0 <= nx < c):
                    continue
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                if islands[ny][nx] == 0:
                    table[ny][nx] = table[y][x] + 1
                    q.append((ny, nx))
                elif islands[ny][nx] != island_num and table[y][x] >= 2:
                    edges.append((table[y][x], island_num, islands[ny][nx]))

                    
n = make_islands() - 1
find_routes()
parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges.sort()
total, cnt = 0, 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost
        cnt += 1
        if cnt == n-1:
            break

if cnt == n-1:
    print(total)
else:
    print(-1)