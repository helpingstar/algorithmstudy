import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = 100000

distance = [INF] * 10001
n_road, target = map(int, input().split())
graph = defaultdict(list)
jirm_set = set()
for _ in range(n_road):
    a, b, c = map(int, input().split())
    if b > target:
        continue
    graph[a].append((b, c))
    jirm_set.add(a)

jirm_set.add(target)

# print(graph)
# print(f'[debug]  jirm_set: {jirm_set}')
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        dist, now = heapq.heappop(q)
        # print(f'[debug] now: {now}, dist: {dist}')
        if now == target:
            return dist
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                heapq.heappush(q, (cost, next))

        for jirm in jirm_set:
            if jirm <= now:
                continue
            if dist + (jirm - now) < distance[jirm]:
                heapq.heappush(q, (dist+jirm-now, jirm))

print(dijkstra())
