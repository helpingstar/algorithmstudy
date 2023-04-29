import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N = int(input())
    rankings = list(map(int, input().split()))

    o_rank = [-1] * (N+1)

    graph = [[] for _ in range(N+1)]
    degree = [0] * (N+1)

    for i, rank in enumerate(rankings):
        graph[rank] = rankings[i+1:]
        degree[rank] = i
        o_rank[rank] = i

    for _ in range(int(input())):
        a, b = map(int, input().split())
        if o_rank[a] < o_rank[b]:
            graph[a].remove(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            degree[a] -= 1
            degree[b] += 1
    q = deque()
    ans = []
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        ans.append(now)
        for nxt in graph[now]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

    if len(ans) == N:
        print(*ans)
    else:
        print("IMPOSSIBLE")


for _ in range(int(input())):
    solution()
