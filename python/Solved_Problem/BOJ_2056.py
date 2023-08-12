import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    cost = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    track = [0] * (N + 1)
    indegree = [0] * (N + 1)
    for i in range(1, N + 1):
        line = list(map(int, input().split()))
        cost[i] = line[0]
        indegree[i] = line[1]
        for j in line[2:]:
            graph[j].append(i)
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            track[i] = cost[i]
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            track[nxt] = max(track[nxt], track[now] + cost[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
    print(max(track))

solution()
