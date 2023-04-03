import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0


def dfs(now, step):
    # print(f'now: {now}, step: {step}')
    global result
    global N
    if step == 5:
        result = 1
        return True

    for nxt in graph[now]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        if dfs(nxt, step+1):
            return True
        visited[nxt] = False
    return False


for i in range(N):
    visited[i] = True
    if dfs(i, 1):
        break
    visited[i] = False

print(result)
