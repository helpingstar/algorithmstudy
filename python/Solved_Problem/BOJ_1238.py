import sys
import heapq

input = sys.stdin.readline


def solution():
    N, M, X = map(int, input().split())
    inner_graph = [[] for _ in range(N+1)]
    outer_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        inner_graph[a].append((b, c))
        outer_graph[b].append((a, c))

    def dijkstra(start, graph: list):
        distance = [float('inf')] * (N+1)
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

    inner_distance = dijkstra(X, inner_graph)
    outer_distance = dijkstra(X, outer_graph)
    ans = 0
    for i in range(1, N+1):
        ans = max(ans, inner_distance[i]+outer_distance[i])

    print(ans)


solution()
