import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
dp = [[0] * C for _ in range(R)]

ans = 0

for r in range(R):
    for c in range(C):
        if r == 0 or c == 0:
            if board[r][c] == '1':
                dp[r][c] = 1
        elif board[r][c] == '1':
            dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
        ans = max(ans, dp[r][c])

print(ans*ans)
