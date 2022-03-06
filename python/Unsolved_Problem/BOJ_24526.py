import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    indegree[a] += 1
    
def topology_sort():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)
    
    while q:
        t = q.popleft()
        for i in graph[t]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                result.append(i)
    return result

print(len(topology_sort()))