import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(V, E):
    total = 0
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        total += c
        edges.append((c, a, b))

    edges.sort()
    parent = [i for i in range(V+1)]


    for c, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total -= c
    return total

while True:
    V, E = map(int, input().split())
    if (V, E) == (0, 0):
        break
    else:
        print(solution(V, E))