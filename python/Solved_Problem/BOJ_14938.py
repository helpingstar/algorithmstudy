import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = 10000
n_region, n_range, n_road = map(int, input().split())

items = [0] + list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(n_road):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n_region+1)
    total_item = 0
    item_visited = [False] * (n_region+1)
    distance[start] = 0
    q = []
    q.append((0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if not item_visited[now]:
            if dist <= n_range:
                total_item += items[now]
                item_visited[now] = True

        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return total_item

ans = 0
for i in range(1, n_region):
    ans = max(ans, dijkstra(i))
print(ans)
