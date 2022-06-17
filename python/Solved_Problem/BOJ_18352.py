import sys
import heapq

input = sys.stdin.readline

v, e, d, s = map(int, input().split())

graph = [[] for _ in range(v+1)]
INF = 10e9
distance = [INF] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(s)

equal = []


for i in range(1, v+1):
    if distance[i] == d:
        equal.append(i)

if equal:
    print(*equal, sep='\n')
else:
    print(-1)