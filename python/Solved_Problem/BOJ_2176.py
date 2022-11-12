import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

n_vertex, n_edge = map(int, input().split())

graph = [[] for _ in range(n_vertex+1)]

for _ in range(n_edge):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF] * (n_vertex + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
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

dist = dijkstra(2)
visited = [False] * (n_vertex + 1)
road = [0] * (n_vertex + 1)
road[2] = 1

# print(f'road  : {road}')
# print(f'dist  : {dist}')

def dp(x):
    # print(f'now : {x}')
    if road[x]:
        return road[x]
    for next, _ in graph[x]:
        if dist[next] < dist[x]:
            # print(f'x : {x}, next : {next}')
            road[x] += dp(next)
            # print(f'road[x] : {road[x]}')
    return road[x]

dp(1)

# print(f'road  : {road}')

print(road[1])
