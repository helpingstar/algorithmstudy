import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def solution():
    v, e = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    cost = [0] * (v+1)
    degree = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
    target = int(input())
    
    q = deque()
    
    for i in range(1, v+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            cost[next] = max(cost[next], time[now]+cost[now])
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)
    
    return cost[target] + time[target]
    

for _ in range(T):
    print(solution())
    