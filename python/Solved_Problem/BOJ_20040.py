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
        

v, e = map(int, input().split())

parent = [i for i in range(v)]

union_list = []

for i in range(e):
    a, b = map(int, input().split())
    union_list.append((a, b))

cnt = 0
for a, b in union_list:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        cnt += 1
    else:
        break

if cnt == e:
    print(0)
else:
    print(cnt+1)