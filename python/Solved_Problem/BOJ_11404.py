import sys

input = sys.stdin.readline
INF = int(1e10)

n = int(input())
m = int(input())

matrix = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if matrix[a][b] > c:
        matrix[a][b] = c


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min((matrix[i][j], matrix[i][k] + matrix[k][j]))

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == INF:
            matrix[i][j] = 0

for i in range(1, n+1):
    print(*matrix[i][1:])