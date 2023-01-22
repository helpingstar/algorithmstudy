import sys

input = sys.stdin.readline

n_size = int(input())

board = [list(map(int, input().split())) for _ in range(n_size)]
ans = 0

ans_board = [[0] * n_size for _ in range(n_size)]
ans_board[0][0] = 1
for i in range(n_size):
    x, y = (i, 0)
    for j in range(i+1):
        nx, ny = x - j, y + j
        # print(nx, ny)
        step = board[nx][ny]
        if nx + step < n_size:
            ans_board[nx+step][ny] += ans_board[nx][ny]
        if ny + step < n_size:
            ans_board[nx][ny+step] += ans_board[nx][ny]

for i in range(n_size-1, 1, -1):
    x, y = (n_size-1, n_size - i)
    # print(f'[debug] x, y : {x, y}')
    for j in range(i):
        nx, ny = x - j, y + j
        # print(f'[debug] nx, ny : {nx, ny}')
        step = board[nx][ny]
        if nx + step < n_size:
            ans_board[nx+step][ny] += ans_board[nx][ny]
        if ny + step < n_size:
            ans_board[nx][ny+step] += ans_board[nx][ny]

print(ans_board[n_size-1][n_size-1])
