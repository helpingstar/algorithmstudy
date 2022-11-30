import sys

input = sys.stdin.readline

INF = sys.maxsize

n_star = int(input())
star_pos = []
# graph = [[INF] * n_star for _ in range(n_star)]
edges = []
dist = [[INF] * n_star for _ in range(n_star)]
for i in range(n_star):
    dist[i][i] = 0

for i in range(n_star):
    x, y, z = map(int, input().split())
    star_pos.append((x, y, z))


for i in range(n_star):
    for j in range(i+1):
        dist = min(abs(star_pos[i][0] - star_pos[j][0]), abs(star_pos[i][1] - star_pos[j][1]), abs(star_pos[i][2] - star_pos[j][2]))
        # graph[i][j] = dist
        # graph[j][i] = dist
        if i != j:
            edges.append((dist, j, i))

edges.sort()

for i in range(n_star-1):
    for dist, a, b in edges:
        if dist[a][b] <
