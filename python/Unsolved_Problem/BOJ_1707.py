import sys

input = sys.stdin.readline

T = int(input())

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

def solution():
    v, e = map(int, input().split())
    parent = [i for i in range(v+1)]
    
    # graph = [[] for _ in range(v+1)]
    is_cycle = False
    for _ in range(e):
        a, b = map(int, input().split())
        if find(parent, a) == find(parent, b):
            is_cycle = True
        else:
            union(parent, a, b)
            
    if is_cycle:
        return 'NO'
    else:
        return 'YES'

for _ in range(T):
    print(solution())