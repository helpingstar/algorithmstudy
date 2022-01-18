from dis import dis
import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

INF = int(1e9)
x_start_table = [INF] * (n+1)
x_start_table[x] = 0

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))


q = []
heapq.heappush(q, (0, x))
while q:
    dist, now = heapq.heappop(q)
    if x_start_table[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < x_start_table[i[0]]:
            x_start_table[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
            
def distance_to_x(n, start, end):
    if start == end:
        return 0
    q = []
    n_start_table = [INF] * (n+1)
    n_start_table[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if n_start_table[now] < dist:
            continue
        if now == end:
            return n_start_table[end]
        for i in graph[now]:
            cost = dist + i[1]
            if cost < n_start_table[i[0]]:
                n_start_table[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
result = []
# INF 가 아닌것만 가려고 했으나 모든 마을은 길이 있다 하여 모두 돈다
for i in range(1, n+1):
    result.append(x_start_table[i] + distance_to_x(n, i, x))
    
print(max(result))