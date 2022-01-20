import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if now == end:
            return distance[now]
        for next, bus in graph[now]:
            cost = distance[now] + bus
            if cost < distance[next]:
                heapq.heappush(q, (cost, next))
                distance[next] = cost

print(dijkstra(start, end))