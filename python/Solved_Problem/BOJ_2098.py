import sys

input = sys.stdin.readline

n_city = int(input())
INF = int(1e10)
graph = [list(map(int, input().split())) for _ in range(n_city)]
dist = [[0 for _ in range(1 << n_city)] for _ in range(n_city)]

def dp(now, visited):
    # print(f'[debug]  now: {now}, visited: {visited}')
    if visited == (1 << n_city) - 1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return INF

    if dist[now][visited]:
        return dist[now][visited]

    n_min = INF
    for next in range(n_city):
        if visited & (1 << next):
            continue
        if not graph[now][next]:
            continue
        n_min = min(n_min, graph[now][next] + dp(next, visited | (1 << next)))

    dist[now][visited] = n_min
    return dist[now][visited]

ans = dp(0, 1)
print(ans)
