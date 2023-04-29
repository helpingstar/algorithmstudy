import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E, S = map(int, input().split())

graph = [[] for _ in range(V+1)]
depth = [-1] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(now, d):
    depth[now] = d

    for nxt in sorted(graph[now]):
        if depth[nxt] == -1:
            dfs(nxt, d+1)


dfs(S, 0)
print(*depth[1:], sep='\n')
