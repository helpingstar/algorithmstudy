import sys

input = sys.stdin.readline

n_city = int(input())

parent = [i for i in range(n_city+1)]

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

for _ in range(n_city-2):
    a, b = map(int, input().split())
    union(parent, a, b)
    
first = find(parent, 1)
for i in range(2, n_city+1):
    if first != find(parent, i):
        print(first, i)
        break