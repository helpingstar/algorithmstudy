import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(len(line) // 2 - 1):
        graph[i].append((line[2*j+1], line[2*j+2]))


def dijkstra(start, n, have_to):
    distance = [INF] * (n+1)
    q = []
    dist_list = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        dist_list.append(dist)
        if now in have_to:
            have_to.remove(now)
        if not have_to:
            return max(dist_list)
        for end, road in graph[now]:
            cost = dist + road
            if cost < distance[end]:
                heapq.heappush(q, (cost, end))
                distance[end] = cost
    return max(dist_list)

max_dist = -1
for i in range(1, n+1):
    have_to = set([i for i in range(i+1, n+1)])
    max_dist = max(max_dist, dijkstra(i, n, have_to))

print(max_dist)