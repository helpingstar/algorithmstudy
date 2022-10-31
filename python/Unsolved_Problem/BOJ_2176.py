import sys
import heapq
from collections import deque

INF = sys.maxsize

input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    

def dijkstra(start):
    distance = [INF] * (v+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance

dist_2 = dijkstra(2)

def bfs():
    ans = 0
    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        if now == 2:
            ans += 1
            continue
        for next, _ in graph[now]:
            if dist_2[next] < dist_2[now]:
                q.append(next)
    return ans

print(bfs())