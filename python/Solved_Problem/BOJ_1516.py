import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
dist = [0] * (N+1)
degree = [0] * (N+1)
time = [0] * (N+1)

for now in range(1, N+1):
    line = list(map(int, input().split()))
    time[now] = line[0]
    for prev in line[1:-1]:
        degree[now] += 1
        graph[prev].append(now)

q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    dist[now] += time[now]
    for nxt in graph[now]:
        degree[nxt] -= 1
        dist[nxt] = max(dist[nxt], dist[now])
        if degree[nxt] == 0:
            q.append(nxt)

print(*dist[1:], sep='\n')
