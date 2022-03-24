import sys
from collections import deque

input = sys.stdin.readline
# 세로 : n, 가로 : m
n, m = map(int, input().split())

terrain = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# land[(x, y)] = n : x, y좌표는 n섬에 속한다.
land = dict()
landArr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬 구분하여 좌표 구하기, BFS
landNum = 0
for i in range(n):
    for j in range(m):
        if terrain[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            land[(i, j)] = landNum
            landArr.append((i, j, landNum))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and terrain[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        land[(nx, ny)] = landNum
                        landArr.append((nx, ny, landNum))
            landNum += 1

# 다리 제작
edges = []
for x, y, curLand in landArr:
    for i in range(4):
        dist = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if 0 <= nx < n and 0 <= ny < m:
                # dict.get(key) : key에 대응되는 dict의 Value를 준다.
                # land.get((dx, dy)) : (dx, dy)의 섬 번호를 반환
                toLand = land.get((nx, ny))
                if curLand == toLand:
                    break
                if toLand == None:
                    nx += dx[i]
                    ny += dy[i]
                    dist += 1
                    continue
                if dist < 2:
                    break
                edges.append((dist, curLand, toLand))
                break
            else:
                break

edges.sort(reverse=True)

# 크루스칼

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

result = 0
cnt = landNum - 1
parent = [i for i in range(landNum)]

while cnt:
    try:
        cost, a, b = edges.pop()
    except:
        print(-1)
        sys.exit()
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        cnt -= 1

print(result)