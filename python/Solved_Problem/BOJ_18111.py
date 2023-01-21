import sys

input = sys.stdin.readline

board = [[0] * 15 for _ in range(15)]
for i in range(15):
    board[0][i] = i

for r in range(1, 15):
    for c in range(1, 15):
        board[r][c] = board[r-1][c] + board[r][c-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(board[k][n])
