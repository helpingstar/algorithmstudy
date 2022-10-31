import sys

input = sys.stdin.readline

T = int(input())
INF = sys.maxsize

def df():
    edges = []
    n_v, n_e, n_w = map(int, input().split())
    cost = [[10000] * (n_v+1) for _ in range(n_v+1)]
    for _ in range(n_e):
        a, b, c = map(int, input().split())
        if cost[a][b] == 10000:
            edges.append((a, b))
        if cost[b][a] == 10000:
            edges.append((b, a))
        cost[a][b] = min(cost[a][b], c)
        cost[b][a] = min(cost[b][a], c)
    for _ in range(n_w):
        a, b, c = map(int, input().split())
        if cost[a][b] == 10000:
            edges.append((a, b))
        cost[a][b] = min(cost[a][b], -c)

    dist = [INF] * (n_v+1)
    for i in range(n_v):
        for a, b in edges:
            if dist[b] > dist[a] + cost[a][b]:
                dist[b] = dist[a] + cost[a][b]
                if i == n_v -1:
                    return True
    return False


for _ in range(T):
    if df():
        print('YES')
    else:
        print('NO')
