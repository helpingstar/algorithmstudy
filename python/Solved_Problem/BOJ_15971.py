import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
def solution():
    N, start, end = map(int, input().split())


    if N <= 2:
        return 0

    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))


    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    track = [0] * (N+1)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nxt, new_dist in graph[now]:
            cost = dist + new_dist
            if distance[nxt] > cost:
                distance[nxt] = cost
                track[nxt] = (now, new_dist)
                heapq.heappush(q, (cost, nxt))

    cur = end
    trace = []
    while cur != start:
        trace.append(track[cur][1])
        cur = track[cur][0]

    if not trace:
        trace = [0]

    return distance[end] - max(trace)

print(solution())
