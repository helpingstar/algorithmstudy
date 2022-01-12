def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)

n = int(input())
score = list(map(int, input().split()))

stack = []

matrix = [[]]
for _ in range(n):
    matrix.append(list(map(int, input().split()[1:])))

visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if dfs(matrix, i, visited)

print(count)