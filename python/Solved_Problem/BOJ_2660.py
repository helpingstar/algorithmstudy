import sys
import heapq
input = sys.stdin.readline

INF = 100

N = int(input())

graph = [[] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for ne in graph[now]:
            cost = distance[now] + 1
            if cost < distance[ne]:
                distance[ne] = cost
                heapq.heappush(q, (cost, ne))
    return distance

result = []

for i in range(1, N+1):
    result.append((max(dijkstra(i)[1:]), i))

result.sort()

ans = []

for score, i in result:
    if score == result[0][0]:
        ans.append(i)

print(result[0][0], len(ans))
print(*ans)