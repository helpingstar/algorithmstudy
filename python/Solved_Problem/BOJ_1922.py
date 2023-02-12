import sys
from collections import defaultdict

input = sys.stdin.readline

n_com = int(input())
n_line = int(input())

graph = []

parent = [i for i in range(n_com+1)]

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

for _ in range(n_line):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
cnt = 0
answer = 0
for c, a, b in graph:
    if find(parent, a) != find(parent, b):
        cnt += 1
        union(parent, a, b)
        answer += c
        if cnt == n_com - 1:
            break

print(answer)