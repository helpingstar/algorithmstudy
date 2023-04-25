import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[1] = True

for _ in range(int(input())):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

q = deque([(1, 0)])
ans = 0

while q:
    now, step = q.popleft()
    for nxt in graph[now]:
        if visited[nxt]:
            continue
        if step <= 1:
            q.append((nxt, step+1))
            visited[nxt] = True
            ans += 1
print(ans)
