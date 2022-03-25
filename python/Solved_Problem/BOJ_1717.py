import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    if cal == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
