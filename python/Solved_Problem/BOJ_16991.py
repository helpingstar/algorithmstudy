import sys

input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[0 for _ in range(n)] for _ in range(n)]
pos = [tuple(map(int, input().split())) for _ in range(n)]

dist = [[0] * (1 << n) for _ in range(n)]

for i in range(n):
    for j in range(i):
        distance = ((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1]) ** 2) ** 0.5
        graph[i][j] = distance
        graph[j][i] = distance

def dp(now, visited):
    if visited == (1 << n) - 1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return INF

    if dist[now][visited]:
        return dist[now][visited]

    n_min = INF
    for next in range(n):
        if visited & (1 << next):
            continue
        n_min = min(n_min, graph[now][next]+dp(next, visited | (1 << next)))
    dist[now][visited] = n_min

    return dist[now][visited]

ans = dp(0, 1)
print(ans)
