import sys
from collections import deque

input = sys.stdin.readline

V, E, R = map(int, input().split())

graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(R)
visited[R] = True
rank = [0] * (V+1)

cnt = 1
while q:
    now = q.popleft()
    rank[now] = cnt
    cnt += 1
    for nxt in sorted(graph[now], reverse=True):
        if visited[nxt]:
            continue
        visited[nxt] = True
        q.append(nxt)

print(*rank[1:], sep='\n')
