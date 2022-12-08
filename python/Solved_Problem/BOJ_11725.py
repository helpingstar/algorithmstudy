import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
graph = defaultdict(list)
visited = [False] * (n+1)
visited[1] = True
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    for next in graph[now]:
        if visited[next]:
            continue
        parent[next] = now
        visited[next] = True
        dfs(next)

dfs(1)
print(*parent[2:], sep='\n')
