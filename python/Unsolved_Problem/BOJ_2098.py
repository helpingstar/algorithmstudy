import sys

input = sys.stdin.readline

n_city = int(input())
graph = [list(map(int, input().split())) for _ in range(n_city)]
INF = int(1e9)

board = [[0] * (1 << n_city) for _ in range(n_city)]

def tsp(now, visited):
    if visited == (1 << n_city) - 1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return INF

    if board[now][visited]:
        return board[now][visited]

    n_min = INF
    for next in range(1, n_city):
        if not graph[now][next]:
            continue
        if visited & (1 << next):
            continue
        n_min = min(n_min, graph[now][next] + tsp(next, visited | 1 << next))
    board[now][visited] = n_min

    return board[now][visited]

print(tsp(0, 1))
