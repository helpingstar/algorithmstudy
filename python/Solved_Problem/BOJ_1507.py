import sys
import heapq
input = sys.stdin.readline
n_city = int(input())

INF = sys.maxsize
board = [list(map(int, input().split())) for _ in range(n_city)]
graph = [[] for _ in range(n_city)]
all_graph = []

for i in range(n_city):
    for j in range(i+1, n_city):
        all_graph.append((board[i][j], i, j))

all_graph.sort()


def dijkstra(start):
    distance = [INF] * n_city
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for new_dist, nxt in graph[now]:
            cost = dist + new_dist
            if distance[nxt] > cost:
                heapq.heappush(q, (cost, nxt))
                distance[nxt] = cost
    return distance


result = 0
impossible = False
for c, s, e in all_graph:
    dist = dijkstra(s)
    # print(graph)
    if dist[e] > c:
        graph[s].append((c, e))
        graph[e].append((c, s))
        result += c
        # print(c, s, e)
    elif dist[e] < c:
        impossible = True
        break

if impossible:
    print(-1)
else:
    print(result)
