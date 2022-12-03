import sys

input = sys.stdin.readline

r, c = map(int, input().split())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
board = [list(input().rstrip()) for _ in range(r)]

trace = set()

trace.add((0, 0, board[0][0], 1))
ans = 1

while trace:
    x, y, visited, count = trace.pop()
    # print(f'[debug]  x:{x}, y:{y}')
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print(f'[debug]   nx:{nx}, ny:{ny}')
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        if board[nx][ny] in visited:
            continue
        trace.add((nx, ny, visited + board[nx][ny], count+1))
        ans = max(count+1, ans)

print(ans)
