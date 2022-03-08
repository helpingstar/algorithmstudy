import sys
import heapq

input = sys.stdin.readline
INF = 1e9
v, e = map(int, input().split())

start = int(input())
distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for end, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[end] > cost:
                distance[end] = cost
                heapq.heappush(q, (cost, end))
    return distance

for i in dijkstra(start)[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)