import sys

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_row, n_col = map(int, input().split())

board = []
for _ in range(n_row):
    board.append(list(input().rstrip()))

visited = set()
visited_word = set()
ans = 0

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    # print(f'[debug]  (x, y) : {(x, y)}')
    # print(f'[debug]  visited: {visited}')
    visited.add((x, y))
    visited_word.add(board[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n_row and 0 <= ny < n_col):
            continue
        if (nx, ny) in visited:
            continue
        if board[nx][ny] in visited_word:
            continue
        dfs(nx, ny, count+1)
    visited.remove((x, y))
    visited_word.remove(board[x][y])

dfs(0, 0, 0)
print(ans+1)
