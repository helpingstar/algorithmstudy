import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = sys.maxsize
score = [[INF] * (k+1) for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    
def dijkstra(start):
    # for i in range(k+1):
    #     score[start][i] = 0
    score[start][0] = 0
    q = []
    heapq.heappush(q, (0, start, 0))
    while q:
        dist, now, count = heapq.heappop(q)
        if score[now][count] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = dist + new_dist
            if count == k:
                if cost < score[next][k]:
                    score[next][k] = cost
                    heapq.heappush(q, (cost, next, count))
            else:
                if cost < score[next][count]:
                    score[next][count] = cost
                    heapq.heappush(q, (cost, next, count))
                if dist < score[next][count+1]:
                    score[next][count+1] = dist
                    heapq.heappush(q, (dist, next, count+1))

dijkstra(1)
print(min(score[n]))
            