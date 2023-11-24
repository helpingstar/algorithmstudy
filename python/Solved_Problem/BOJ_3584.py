import sys

input = sys.stdin.readline
LOG = 21
sys.setrecursionlimit(10**7)


def solution():
    def assgin_depth(now, d):
        visited[now] = True
        depth[now] = d
        for nxt in graph[now]:
            if visited[nxt]:
                continue
            parent[nxt][0] = now
            assgin_depth(nxt, d+1)

    n_node = int(input())

    parent = [[0] * LOG for _ in range(n_node+1)]
    depth = [0] * (n_node + 1)
    visited = [False] * (n_node + 1)
    is_root = [True] * (n_node + 1)
    graph = [[] for _ in range(n_node+1)]
    for _ in range(n_node-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        is_root[b] = False

    for i in range(1, n_node):
        if is_root[i]:
            root = i
            break

    assgin_depth(root, 1)
    a, b = map(int, input().split())

    for i in range(1, LOG):
        for j in range(1, n_node+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

    # a가 더 깊어진다.
    if depth[a] < depth[b]:
        a, b = b, a

    for i in range(LOG-1, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


for _ in range(int(input())):
    print(solution())
