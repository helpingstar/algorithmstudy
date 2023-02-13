n = int(input())

board = [[' '] * (2 * n) for _ in range(n)]

def dp(x, y, cnt):
    if cnt == 3:
        board[x][y] = '*'
        board[x+1][y-1] = '*'
        board[x+1][y+1] = '*'
        for i in range(5):
            board[x+2][y-2+i] = '*'
        return

    cnt //= 2
    dp(x, y, cnt)
    dp(x+cnt, y-cnt, cnt)
    dp(x+cnt, y+cnt, cnt)

dp(0, n-1, n)

for line in board:
    print(*line, sep='')
