import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
parent = [i for i in range(v+1)]
edges = []

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    edges.append((a, b))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges.sort()

for edge in edges:
    x, y = edge
    union_parent(parent, x, y)

result = set()

for i in range(1, v+1):
    result.add(parent[i])

print(len(result))