import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = 1000
n_member = int(input())

n_edge = int(input())
parent = [i for i in range(n_member + 1)]
graph = [[] for _ in range(n_member+1)]
edges = []

for _ in range(n_edge):
    a, b = map(int, input().split())
    edges.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

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

for a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

def dijkstra(start):
    q = []
    distance = [INF] * (n_member + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    max_dist = 0
    for d in distance:
        if d == 0 or d == INF:
            continue
        if d > max_dist:
            max_dist = d
    return max_dist

committee = defaultdict(list)

for i in range(1, n_member+1):
    committee[find_parent(parent, i)].append(i)
    
# print(parent)
print(len(committee))
ans = []
for i, members in committee.items():
    min_value = INF
    index = members[0]
    for j in members:
        temp = dijkstra(j)
        if temp < min_value:
            index = j
            min_value = temp
    ans.append(index)

ans.sort()
print(*ans, sep='\n')