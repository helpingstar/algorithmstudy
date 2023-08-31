import sys
from collections import deque

input = sys.stdin.readline

def solution():
    cnt = 0
    while True:
        a, b = map(int, input().split())
        if a == 0:
            return
        cnt += 1
        result = topology(a, b)

        if result == 0:
            print(f"Case {cnt}: No trees.")
        elif result == 1:
            print(f"Case {cnt}: There is one tree.")
        else:
            print(f"Case {cnt}: A forest of {result} trees.")

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def topology(V, E):
    degree = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    parent = [i for i in range(V + 1)]
    is_cycle = [False] * (V + 1)
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        union(parent, a, b)
        graph[a].append(b)
        graph[b].append(a)

        degree[a] += 1
        degree[b] += 1

    result = 0
    q = deque()
    for i in range(1, V + 1):
        if degree[i] == 0:
            result += 1
            visited[i] = True
        if degree[i] == 1:
            q.append(i)

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            degree[now] -= 1
            degree[nxt] -= 1

            if degree[nxt] == 1:
                q.append(nxt)

    for i in range(1, V + 1):
        if degree[i] > 0:
            is_cycle[find(parent, i)] = True
    for i in range(1, V + 1):
        pnt = find(parent, i)
        if not visited[pnt] and not is_cycle[pnt]:
            result += 1
            visited[i] = True

    return result


solution()
