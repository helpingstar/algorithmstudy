import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

temp_board = [[0] * C for _ in range(R)]

for r in range(R):
    temp_board[r][0] = board[r][0]
    for c in range(1, C):
        temp_board[r][c] = temp_board[r][c-1] + board[r][c]

# sum_board = [[0] * C for _ in range(R)]

# for c in range(C):
#     sum_board[0][c] = temp_board[0][c]
#     for r in range(1, R):
#         sum_board[r][c] = sum_board[r-1][c] + temp_board[r][c]

for _ in range(int(input())):
