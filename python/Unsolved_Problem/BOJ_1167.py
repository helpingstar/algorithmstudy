import sys
input = sys.stdin.readline

graph = 

# 각 그래프를 거리로 초기화
for _ in range(n):
    line = list(map(int, input().split()))
    if len(line) == 1:
        continue
    for i in range(len(line) // 2 - 1):
        graph[line[0]][line[i*2 + 1]] = line[i*2 + 2]


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_num = -1
for i in range(1, n+1):
    for j in range(1, n+1):
        max_num = max(max_num, graph[i][j])

print(max_num)