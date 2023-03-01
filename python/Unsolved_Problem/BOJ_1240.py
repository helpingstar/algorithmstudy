import sys

input = sys.stdin.readline
INF = int(1e10)
n_node, n_dist = map(int, input().split())

dist = [[INF] * n_node for _ in range(n_node)]
graph = [[[] for _ in range(n_node+1)]]

for _ in range(n_node-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

for i in range(n_node):
    for j in range(n_node):
        for k in range(n_node):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for _ in range(n_dist):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    print(dist[a][b])
