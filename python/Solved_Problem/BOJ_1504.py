import sys
import heapq

input = sys.stdin.readline

def solution():
    INF = int(1e10)
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    def dijkstra(start):
        distance = [INF] * (V+1)
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for nxt, new_dist in graph[now]:
                cost = dist + new_dist
                if distance[nxt] <= cost:
                    continue
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
        return distance

    v1_dist = dijkstra(v1)
    v2_dist = dijkstra(v2)
    common = v1_dist[v2]

    ans = min(v2_dist[1] + common + v1_dist[V], v1_dist[1] + common + v2_dist[V])
    if ans >= INF:
        print(-1)
    else:
        print(ans)

solution()
