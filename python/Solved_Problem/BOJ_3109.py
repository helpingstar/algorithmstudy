import sys

input = sys.stdin.readline
R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

ans = 0

def dfs(x, y):
    global ans
    if y == C-1:
        board[x][y] = 'x'
        ans += 1
        return True

    for nx in [x-1, x, x+1]:
        if not (0 <= nx < R):
            continue
        if board[nx][y+1] == 'x':
            continue
        board[nx][y+1] = 'x'
        if dfs(nx, y+1):
            return True

for i in range(R):
    board[i][0] = 'x'
    dfs(i, 0)


print(ans)
