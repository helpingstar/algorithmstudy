import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, E, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
cnt = 2
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now):
    global cnt

    for nxt in sorted(graph[now]):
        if visited[nxt] != -1:
            continue
        visited[nxt] = cnt

        cnt += 1
        dfs(nxt)


visited[R] = 1
dfs(R)

for v in visited[1:]:
    if v == -1:
        print(0)
    else:
        print(v)
