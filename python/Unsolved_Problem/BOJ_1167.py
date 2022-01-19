import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(1, n+1):
    line = list(map(int, input().split()))
    start_node = line[0]
    for j in range(len(line) // 2 - 1):
        graph[start_node].append((line[2*j+1], line[2*j+2]))


def dijkstra(start, n, stop = None):
    distance = [INF] * (n+1)
    distance[0] = 0
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for end, road in graph[now]:
            cost = dist + road
            if cost < distance[end]:
                heapq.heappush(q, (cost, end))
                distance[end] = cost
    return distance

start_table = dijkstra(1, n)
start_dist = max(start_table)
longest_from_start = start_table.index(start_dist)

end_dist = max(dijkstra(longest_from_start, n))

print(end_dist)