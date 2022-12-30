import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
n_vertex, n_edge = map(int, input().split())

graph = [[] for _ in range(n_vertex+1)]

for _ in range(n_edge):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n_vertex+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance

def dijkstra2(start):
    distance = [[INF, INF] for _ in range(n_vertex + 1)]
    distance[start] = [INF, 0]
    q = []
    heapq.heappush(q, (0, start, True))
    while q:
        dist, now, fast = heapq.heappop(q)
        if distance[now][fast] < dist:
            continue
        for next, new_dist in graph[now]:
            if fast:
                cost = dist + new_dist / 2
            else:
                cost = dist + new_dist * 2
            if cost < distance[next][not fast]:
                distance[next][not fast] = cost
                heapq.heappush(q, (cost, next, not fast))
    return distance

fox_distance = dijkstra(1)
wolf_distance = dijkstra2(1)


result = 0
for i in range(1, n_vertex+1):
    if fox_distance[i] < min(wolf_distance[i]):
        result += 1

print(result)
