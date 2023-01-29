import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_row, n_col, n_domain = map(int, input().split())

board = [[0] * n_col for _ in range(n_row)]

for _ in range(n_domain):
    lb_c, lb_r, rt_c, rt_r = map(int, input().split())
    for c in range(lb_c, rt_c):
        for r in range(lb_r, rt_r):
            board[r][c] = 1

def bfs(x, y):
    q = deque()
    cnt = 1
    board[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_row and 0 <= ny < n_col):
                continue
            if board[nx][ny] == 1:
                continue
            q.append((nx, ny))
            cnt += 1
            board[nx][ny] = 1
    return cnt
ans = []
for r in range(n_row):
    for c in range(n_col):
        if board[r][c] == 0:
            ans.append(bfs(r, c))

print(len(ans))
print(*sorted(ans))
