import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF] * (V+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for ne, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[ne]:
                distance[ne] = cost
                heapq.heappush(q, (cost, ne))
    return distance

print(dijkstra(1)[V])
