import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

graph = defaultdict(list)
visited = set()
INF = sys.maxsize
answer = 0
cnt = 0
valid = False


def dijkstra(start):
    distance = defaultdict(lambda: INF)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nxt, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return distance


while True:
    try:
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        valid = True

    except:
        if not valid:
            print(0)
            break
        distance1 = dijkstra(a)
        max_dist = 0
        max_idx = 0

        # print(a)
        # print(distance1)
        for i in distance1.keys():
            if distance1[i] > max_dist:
                max_dist = distance1[i]
                max_idx = i

        distance2 = dijkstra(max_idx)
        # print(i)
        # print(distance2)
        print(max(distance2.values()))
        break
