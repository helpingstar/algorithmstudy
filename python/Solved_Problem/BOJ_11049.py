import sys

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
matrix_list = []
dp = [[0] * n for _ in range(n)]

def cal(x, y):
    if y - x == 0:
        return 0
    elif y - x == 1:
        return matrix_list[x][0] * matrix_list[x][1] * matrix_list[y][1]
    else:
        ans = INF
        for i in range(x, y):
            ans = min(ans, dp[x][i] + dp[i+1][y] + matrix_list[x][0] * matrix_list[i][1] * matrix_list[y][1])
        return ans

for _ in range(n):
    a, b = map(int, input().split())
    matrix_list.append((a, b))

for size in range(n):
    for start in range(n-size):
        dp[start][start+size] = cal(start, start+size)

print(dp[0][n-1])