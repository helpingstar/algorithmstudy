import sys

input = sys.stdin.readline

v, e = map(int, input().split())

INF = 1e9

graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def check(n):            
    for i in range(1, v+1):
        if graph[i][n] == INF and graph[n][i] == INF:
            return 0
    return 1

result = 0

for i in range(1, v+1):
    result += check(i)
    
print(result)