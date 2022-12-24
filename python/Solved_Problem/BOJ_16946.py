import sys
from collections import deque
input = sys.stdin.readline

n_row, n_col = map(int, input().split())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

sum_board = [[0] * (n_col) for _ in range(n_row)]
visited = [[False] * (n_col) for _ in range(n_row)]
board = []

for i in range(n_row):
    line = list(map(int, list(input().rstrip())))
    board.append(line)
    # print(f'[debug] line: {line}')
    for j in range(n_col):
        # print(f'[debug]  j: {j}')
        if line[j] == 1:
            sum_board[i][j] += 1

def bfs(x, y):
    n_zero = 1
    one_list = set()
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_row and 0 <= ny < n_col):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                one_list.add((nx, ny))
            else:
                n_zero += 1
                q.append((nx, ny))
                visited[nx][ny] = True
    # print(f'[debug]  one_list: {one_list}')
    # print(f'[debug]  n_zero  : {n_zero}')
    while one_list:
        x, y = one_list.pop()
        sum_board[x][y] += n_zero
        sum_board[x][y] %= 10

for r in range(n_row):
    for c in range(n_col):
        if board[r][c] == 0 and not visited[r][c]:
            bfs(r, c)

for line in sum_board:
    print(*line, sep='')
    