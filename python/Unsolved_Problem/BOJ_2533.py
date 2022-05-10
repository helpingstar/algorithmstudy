import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
edges = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges[a] += 1
    edges[b] += 1

cnt = 0

while sum(edges) != 0:
    now = edges.index(max(edges))
    edges[now] = 0
    for i in graph[now]:
        if edges[i] > 0:
            edges[i] -= 1
    cnt += 1

print(cnt)