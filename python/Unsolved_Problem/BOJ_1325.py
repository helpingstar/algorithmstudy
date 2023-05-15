import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_max = 0
ans = set()
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[b].append(a)

def dfs(origin, x, count):
    global n_max
    global ans
    # print(f'[debug]  origin, x, count: {origin, x, count}')
    if count > n_max:
        n_max = count
        ans = {origin}
    elif count == n_max:
        ans.add(origin)

    for nxt in graph[x]:
        visited[nxt] = True
        dfs(origin, nxt, count+1)
        visited[nxt] = False

for i in range(1, n+1):
    visited[i] = True
    dfs(i, i, 1)
    visited[i] = False

print(*sorted(ans))
