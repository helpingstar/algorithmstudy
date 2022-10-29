import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for r in range(n):
        for c in range(n):
            if board[r][i] and board[i][c]:
                board[r][c] = 1

for line in board:
    print(*line)
