import sys

input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))

is_leaf = [True] * n
# n_child = [0] * n
graph = [[] for _ in range(n)]
total_leaf = n
for i, p in enumerate(parent):
    if p == -1:
        continue
    if is_leaf[p]:
        is_leaf[p] = 0
        total_leaf -= 1
    # n_child[p] += 1
    graph[p].append(i)

delete_node = int(input())


def dfs(now):
    global total_leaf
    if is_leaf[now]:
        total_leaf -= 1
        return
    for nxt in graph[now]:
        dfs(nxt)


if len(graph[parent[delete_node]]) == 1:
    total_leaf += 1

dfs(delete_node)

print(total_leaf)
