import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
v, e, k = map(int, input().split())

graph = [[] for _ in range(v+1)]

distance = [[INF] * (k+1) for _ in range(v+1)]
        
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):  
    q = []
    cnt = 0
    heapq.heappush(q, (0, start, 0))
    distance[start][cnt] = 0
    while q:
        dist, now, cnt = heapq.heappop(q)
        if distance[now][cnt] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[next][cnt] > cost:
                distance[next][cnt] = cost
                heapq.heappush(q, (cost, next, cnt))
            
            if cnt < k and distance[next][cnt+1] > dist:
                distance[next][cnt+1] = dist
                heapq.heappush(q, (dist, next, cnt+1))

dijkstra(1)

print(min(distance[v]))