import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sum_board = [[0] * (n+1) for _ in range(n+1)]

board = [[0] * (n+1)]
for i in range(n):
    line = [0] + list(map(int, input().split()))
    board.append(line)
    for j in range(n):
        sum_board[i+1][j+1] = sum_board[i+1][j] + line[j+1]

total_sum_board = [[0] * (n+1) for _ in range(n+1)]

for c in range(1, n+1):
    for r in range(n):
        total_sum_board[r+1][c] = total_sum_board[r][c] + sum_board[r+1][c]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = total_sum_board[x2][y2]
    result -= total_sum_board[x1-1][y2]
    result -= total_sum_board[x2][y1-1]
    result += total_sum_board[x1-1][y1-1]
    print(result)