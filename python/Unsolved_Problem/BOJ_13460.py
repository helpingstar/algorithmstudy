import sys
from collections import deque
from tabnanny import check

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r_pos = []
b_pos = []
o_pos = []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'R':
            r_pos = [i, j]
        elif board[i][j] == 'B':
            b_pos = [i, j]
        elif board[i][j] == 'O':
            o_pos = (r, c)


def check_board(cur_x, cur_y, dx, dy, board, color):
    nx = cur_x + dx
    ny = cur_y + dy
    if board[ny][nx] in ['#', 'R', 'B']:
        return (cur_y, cur_x)
    while board[ny][nx] not in ['#', 'R', 'B']:
        if board[ny][nx] == 'O':
            if color == 'R':
                return 'R'
            else:
                return 'B'
        pre_x, pre_y = nx, ny
        ny = pre_y + dy
        nx = pre_x + dx
    return (pre_y, pre_x)

    


def bfs(r_pos, b_pos):
    visited_r = [[False] * c for _ in range(r)]
    cnt = 1
    q = deque()
    visited_r[r_pos[0]][r_pos[1]] = True
    q.append((r_pos, b_pos, cnt))
    while q:
        r_cur, b_cur, cnt= q.popleft()
        r_y, r_x = r_cur
        b_y, b_x = b_cur
        for i in range(4):
            if board[r_y+dy[i]][r_x+dx[i]] == '#':
                continue
            if visited_r[r_y+dy[i]][r_x+dx[i]]:
                continue
            r_result = check_board(r_x, r_y, dx[i], dy[i], board, 'R')
            b_result = check_board(b_x, b_y, dx[i], dy[i], board, 'B')
            if b_result == 'B':
                continue
            if r_result == b_result:
                continue
            if r_result == 'R':
                return cnt
            if visited_r[r_result[0]][r_result[1]]:
                continue
            q.append((r_result, b_result, cnt+1))
            # board[r_result[0]][r_result[1]] = 'R'
            # board[b_result[0]][b_result[1]] = 'B'
            # board[r_y][r_x] = '.'
            # board[b_y][b_x] = '.'a
            visited_r[r_result[0]][r_result[1]] = True
    return -1

result = bfs(r_pos, b_pos)

if result > 10:
    print(-1)
else:
    print(result)
            
