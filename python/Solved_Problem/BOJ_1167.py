import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    line = list(map(int, input().split()))
    start = line[0]
    for i in range(len(line) // 2 - 1):
        graph[start].append((line[i*2 + 1], line[i*2 + 2]))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[0] = 0

    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for end, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[end] > cost:
                distance[end] = cost
                heapq.heappush(q, (cost, end))
    return (distance, distance.index(max(distance)))

first = dijkstra(1)

print(max(dijkstra(first[1])[0]))