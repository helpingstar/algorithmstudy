import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N = int(input())
    degree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    time = [0] * (N+1)
    for i in range(1, N+1):
        line = list(map(int, input().split()))
        time[i] = line[0]
        for j in range(1, len(line)-1):
            degree[i] += 1
            graph[line[j]].append(i)

    dist = [0] * (N+1)

    q = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
            dist[i] = time[i]

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            dist[nxt] = max(dist[nxt], dist[now] + time[nxt])
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

    print(*dist[1:], sep='\n')


solution()
