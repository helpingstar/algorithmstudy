import sys

from collections import deque
input = sys.stdin.readline

R, C = 12, 6

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = [list(input().rstrip()) for _ in range(R)]


def bfs(r, c, color, visited):
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = True
    color_list = [(r, c)]
    n_cnt = 1
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == '.':
                continue

            if board[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))
                color_list.append((nx, ny))
                n_cnt += 1
    # print(n_cnt, color)

    if n_cnt >= 4:
        for x, y in color_list:
            board[x][y] = '.'
        return True
    else:
        return False


def puyo():
    visited = [[False] * C for _ in range(R)]
    breaking = False
    for r in range(R):
        for c in range(C):
            if board[r][c] != '.' and not visited[r][c]:
                if bfs(r, c, board[r][c], visited):
                    breaking = True
    return breaking


def drop():
    for c in range(C):
        cur = 11
        for r in range(R-1, -1, -1):
            if board[r][c] != '.':
                board[cur][c] = board[r][c]
                cur -= 1
        for r in range(cur, -1, -1):
            board[r][c] = '.'


cnt = 0
while True:
    if not puyo():
        print(cnt)
        break
    drop()
    cnt += 1
