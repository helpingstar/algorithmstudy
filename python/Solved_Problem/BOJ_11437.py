import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
LOG = 21
n_node = int(input())
visited = [False] * (n_node+1)
graph = defaultdict(list)
depth = [0] * (n_node+1)
parent = [[0] * (LOG) for _ in range(n_node+1)]

for _ in range(n_node-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def assign_depth(now, now_depth, now_parent):
    # print(f'[debug]  now:{now}, now_depth:{now_depth}')
    visited[now] = True
    parent[now][0] = now_parent
    depth[now] = now_depth
    for next in graph[now]:
        if not visited[next]:
            assign_depth(next, now_depth+1, now)

def assign_parent():
    assign_depth(1, 1, 0)
    for i in range(1, LOG):
        for node in range(1, n_node+1):
            parent[node][i] = parent[parent[node][i-1]][i-1]

assign_parent()

def lca(a, b):
    if a == b:
        return a
    if depth[a] > depth[b]: # b의 깊이를 더 깊게한다.
        a, b = b, a
    for i in range(LOG-1, -1, -1):
        if depth[parent[b][i]] >= depth[a]:
            b = parent[b][i]
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]



n_question = int(input())
for _ in range(n_question):
    a, b = map(int, input().split())
    print(lca(a, b))
