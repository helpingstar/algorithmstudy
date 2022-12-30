import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = int(1e9)

T = int(input())

for _ in range(T):
    n_pc, n_depend, hacked = map(int, input().split())
    distance = [INF] * (n_pc+1)
    distance[hacked] = 0
    graph = defaultdict(list)
    for _ in range(n_depend):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    q = []
    heapq.heappush(q, (0, hacked))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    count = 0
    result = 0
    for i in range(1, n_pc+1):
        if distance[i] < INF:
            count += 1
            result = max(result, distance[i])
    print(count, result)
