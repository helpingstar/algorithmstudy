from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())

parent = [i for i in range(n+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    union(parent, a, b)
    graph[a].append(b)
    graph[b].append(a)

def solution():
    if find(parent, start) != find(parent, end):
        return -1
    q = deque()
    q.append((start, 0))
    while q:
        now, cost = q.popleft()
        for i in graph[now]:
            if visited[i]:
                continue
            visited[i] = True
            if i == end:
                return cost + 1
            else:
                q.append((i, cost+1))

print(solution())
