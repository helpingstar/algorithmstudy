import sys
import heapq

n = int(input())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
    distance[0] = 0
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        # print(f'[debug]  {dist, now}')
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                heapq.heappush(q, (cost, next))
                distance[next] = cost
    return distance
if n == 1:
    print(0)
else:
    first = dijkstra(1)
    # print(first)
    max_num = max(first)
    idx = first.index(max_num)
    print(max(dijkstra(idx)))