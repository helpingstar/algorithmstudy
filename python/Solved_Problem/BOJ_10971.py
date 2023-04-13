import sys

input = sys.stdin.readline
INF = int(1e9)
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dist = [[0] * (1 << N) for _ in range(N)]

def dp(now, visited):
    if dist[now][visited]:
        return dist[now][visited]

    if visited == (1 << N) - 1:
        if not graph[now][0]:
            return INF
        else:
            return graph[now][0]

    n_min = INF
    for i in range(N):
        if visited & (1 << i) == 0:
            # if graph[now][i] == 0:
            #     continue
            n_min = min(n_min, graph[now][i] + dp(i, visited | (1 << i)))
    dist[now][visited] = n_min
    return dist[now][visited]

print(dp(0, 1))

# for line in dist:
#     print(line)
