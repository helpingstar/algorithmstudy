import sys
import heapq
from collections import deque

input = sys.stdin.readline

INF = 1e9
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

ans = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
"""
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        distance[now] = dist
        visited[now] = True
        
        for dest, new_dist in graph[now]:
            cost = dist + new_dist
            if visited[dest]:
                continue
            if distance[dest] < cost:
                continue
            heapq.heappush(q, (cost, dest))
"""

def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for dest, new_dist in graph[now]:
            cost = dist + new_dist
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))
        

"""
def bfs(start):
    global ans
    q = deque()
    q.append(start)
    while q:
        now= q.popleft()
        dist = distance[now]
        for dest, _ in graph[now]:
            new_dist = distance[dest]
            if dist < new_dist:
                continue
            if dest == 2:
                ans += 1
            q.append(dest)
            
def dfs(x):
    global ans
    if x == 2:
        ans += 1
    else:
        for dest, _ in graph[x]:
            if distance[dest] < distance[x]:
                dfs(dest)       
"""     

"""
dp를 bottom-up 방식으로 하면 시간 단축할 수 있는데
bfs, dfs로 풀려고 해서 시간초과가 발생하였다.
"""
road = [0] * (n+1)
road[2] = 1
def dp(x):
    if road[x] == 0:
        for next, _ in graph[x]:
            if distance[next] < distance[x]:
                road[x] += dp(next)
    return road[x]

dijkstra2(2)

print(dp(1))
