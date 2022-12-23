import sys

input = sys.stdin.readline

n = int(input())

pos_list = []
for _ in range(n):
    a, b = map(float, input().split())
    pos_list.append((a, b))

edges = []

def get_distance(pos1:list, pos2:list):
    x1, y1 = pos1
    x2, y2 = pos2
    
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for i in range(n-1):
    for j in range(i+1, n):
        dist = get_distance(pos_list[i], pos_list[j])
        edges.append((dist, i, j))
        
edges.sort()

parent = [i for i in range(n)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
count = 0

for dist, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += dist
        count += 1
        if count == n-1:
            break

print(result)