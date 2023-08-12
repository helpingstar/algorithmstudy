import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for i in range(1, N + 1):
        n = int(input())
        indegree[n] += 1
        graph[i].append(n)
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    ans = []
    for i in range(1, N+1):
        if indegree[i] != 0:
            ans.append(i)
    print(len(ans))
    print(*ans, sep='\n')


solution()
