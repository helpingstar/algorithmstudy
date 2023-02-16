import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

# dp[R][C][n]
# [n]
# 0 : -
# 1 : |
# 2 : \
    
for i in range(2, N):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for r in range(1, N):
    for c in range(1, N):
        if board[r][c] + board[r-1][c] + board[r][c-1] == 0:
            dp[r][c][2] = sum(dp[r-1][c-1])
        
        if board[r][c] == 0:
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]

print(sum(dp[N-1][N-1]))
