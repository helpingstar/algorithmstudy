import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    dist = [[-1] * (N + 1) for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    question = [list(map(int, input().split())) for _ in range(K)]
    parent = [[-1, -1] for _ in range(N + 1)]
    depth = [-1] * (N + 1)
    q = deque()
    depth[1] = 0
    q.append(1)
    while q:
        now = q.popleft()
        for s, dist in graph[now]:
            if depth[s] != -1:
                continue
            depth[s] = depth[now] + 1
            q.append(s)
            parent[s] = [now, dist]
    for a, b in question:
        # b 가 더 깊다
        if depth[a] > depth[b]:
            a, b = b, a
        # print(f'[debug] a, b: {a, b}')
        result = 0
        while depth[a] != depth[b]:
            result += parent[b][1]
            b = parent[b][0]
        if a == b:
            print(result)
            continue
        while parent[a][0] != parent[b][0]:
            result += (parent[a][1] + parent[b][1])
            a = parent[a][0]
            b = parent[b][0]
        result += (parent[a][1] + parent[b][1])
        print(result)

solution()
