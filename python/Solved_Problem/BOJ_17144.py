import sys

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if board[i][0] == -1:
        r1 = i
        break

up_list_x = list(range(r1-1, 0, -1)) + [0] * C + list(range(1, r1)) + [r1] * (C-1)
up_list_y = [0] * (r1-1) + list(range(C)) + [C-1] * (r1-1) + list(range(C-1, 0, -1))

down_list_x = list(range(r1+2, R-1)) + [R-1] * C + list(range(R-2, r1+1, -1)) + [r1+1] * (C-1)
down_list_y = [0] * (R - r1 - 3) + list(range(C)) + [C-1] * (R-r1-3) + list(range(C-1, 0, -1))

# print(down_list_x)
# print(down_list_y)

def spread(x, y, new_board):
    if board[x][y] < 5:
        new_board[x][y] += board[x][y]
        return
    mover = board[x][y] // 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < R and 0 <= ny < C) or board[nx][ny] == -1:
            continue
        new_board[nx][ny] += mover
        board[x][y] -= mover
    new_board[x][y] += board[x][y]

def propel(board):
    # up
    for i in range(1, len(up_list_x)):
        x = up_list_x[i]
        y = up_list_y[i]
        px = up_list_x[i-1]
        py = up_list_y[i-1]
        board[px][py] = board[x][y]
    board[r1][1] = 0

    # down
    for i in range(1, len(down_list_x)):
        x = down_list_x[i]
        y = down_list_y[i]
        px = down_list_x[i-1]
        py = down_list_y[i-1]
        board[px][py] = board[x][y]
    board[r1+1][1] = 0

# def pb(board):
#     print('-'*10)
#     for i in board:
#         print(i)
#     print('-'*10)

for _ in range(T):
    new_board = [[0] * C for _ in range(R)]
    new_board[r1][0] = -1
    new_board[r1+1][0] = -1
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                spread(r, c, new_board)
    # pb(new_board)
    propel(new_board)
    # print(f'[debug] after propel')
    # pb(new_board)
    board = new_board

answer = 0
for i in range(R):
    answer += sum(board[i])

print(answer+2)
