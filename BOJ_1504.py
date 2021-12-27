import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
# distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d1, d2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (v+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance
                
t1 = dijkstra(1)
t2 = dijkstra(d1)
t3 = dijkstra(d2)

result = min((t1[d1] + t2[d2] + t3[v], t1[d2] + t3[d1] + t2[v]))

if result >= INF:
    print(-1)
else:
    print(result)