import sys
import heapq
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

n_nodes, n_edges = map(int, input().split())

graph = [[] for _ in range(n_nodes+1)]

for _ in range(n_edges):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF] * (n_nodes + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[next] > cost:
                heapq.heappush(q, (cost, next))
                distance[next] = cost
    return distance

distance_from_2 = dijkstra(2)

road = [0] * (n_nodes + 1)
road[2] = 1

def dp(x):
    if road[x] == 0:
        for next, _ in graph[x]:
            if distance_from_2[next] < distance_from_2[x]:
                road[x] += dp(next)
    return road[x]

print(dp(1))

