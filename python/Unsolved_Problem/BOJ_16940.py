import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)
depth = [0] * (n+1)
test = list(map(int, input().split()))

def dfs(now, d):
    depth[now] = d
    visited[now] = True
    for ne in graph[now]:
        if visited[ne]:
            continue
        dfs(ne, d+1)

dfs(test[0], 1)

is_valid = True
for i in range(n-1):
    if depth[test[i]] > depth[test[i+1]]:
        is_valid = False
        break
# print(depth)
if is_valid:
    print(1)
else:
    print(0)