import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

parent = [0] * (n+1)
edges = []
result = 0
position = []

for i in range(n):
    parent[i] = i

'''
여기서 메모리 초과가 났다.
for i in range(n):
    x, y, z = map(int, input().split())
    for j in range(i):
        edges.append((min(abs(position[j][0] - x), abs(position[j][1]-y), abs(position[j][2]-z)), i, j))
    position.append([x, y, z])
'''

for i in range(n):
    x, y, z = map(int, input().split())
    # 좌표, 인덱스
    position.append((x, y, z, i))

for i in range(3):
    position.sort(key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(position[j - 1][i] - position[j][i]), position[j-1][3], position[j][3]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
    