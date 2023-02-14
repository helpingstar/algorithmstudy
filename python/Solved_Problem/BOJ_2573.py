import sys
from collections import deque, defaultdict
input = sys.stdin.readline
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_row, n_col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n_row)]

def bfs(x, y, visited):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    around = defaultdict(int)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_row and 0 <= ny < n_col):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                around[(x, y)] += 1
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return around

cnt = 0
while True:
    visited = [[False] * n_col for _ in range(n_row)]
    exist = True
    check = 0
    for r in range(n_row):
        for c in range(n_col):
            if board[r][c] > 0 and not visited[r][c]:
                if check > 0:
                    print(cnt)
                    exit(0)
                check += 1
                around = bfs(r, c, visited)
                exist = False
    if exist:
        print(0)
        break
    for (x, y), num in around.items():
        board[x][y] = max(0, board[x][y] - num)
    cnt += 1
