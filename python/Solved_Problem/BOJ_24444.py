import sys
from collections import deque

input = sys.stdin.readline

N, E, start = map(int, input().split())

ans = [start]
q = deque([start])

graph = [[] for _ in range(N+1)]

visited = [0] * (N+1)

visited[start] = 1
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 2
while q:
    now = q.popleft()

    for nxt in sorted(graph[now]):
        if visited[nxt] != 0:
            continue
        q.append(nxt)
        visited[nxt] = cnt
        cnt += 1

print(*visited[1:], sep='\n')
