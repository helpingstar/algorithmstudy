import sys

input = sys.stdin.readline

n = int(input())

board = [[' '] * n for _ in range(n)]

def dp(x, y, num):
    if num == 3:
        for r in range(3):
            for c in range(3):
                board[x+r][y+c] = '*'
        board[x+1][y+1] = ' '
    else:
        num //= 3
        for r in range(3):
            for c in range(3):
                if r == 1 and c == 1:
                    continue
                dp(x + num * r, y + num * c, num)
dp(0, 0, n)
for line in board:
    print(*line, sep='')