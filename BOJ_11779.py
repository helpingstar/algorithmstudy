import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    # a : start / b : end / c : cost
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

first, last = map(int, input().split())

    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0
    while q:
        dist, now, trace = heapq.heappop(q)
        if now == last:
            return (dist, trace)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[0] : now 에서 출발해서 도착할 곳 / i[1] : now -> i[0] 까지 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], trace + [i[0]]))

lowest_cost, cities = dijkstra(first)

print(lowest_cost)
print(len(cities))
print(*cities)