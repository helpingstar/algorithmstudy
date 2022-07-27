import sys

input = sys.stdin.readline

ans = 0
n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

def move(board, way):
    new_board = [[0] * n for _ in range(n)]
    if way == 'up':
        for c in range(n):
            prev = 0
            cnt = 0
            for r in range(n):
                if board[r][c] == 0:
                    continue
                # not 0
                if prev == 0:
                    new_board[cnt][c] = board[r][c]
                    cnt += 1
                    prev = board[r][c]
                else:
                    if board[r][c] == prev:
                        new_board[cnt-1][c] *= 2
                        prev = 0
                    else:
                        new_board[cnt][c] = board[r][c]
                        prev = board[r][c]
                        cnt += 1
            for i in range(cnt, n):
                new_board[i][c] = 0
    elif way == 'down':
        for c in range(n):
            prev = 0
            cnt = n-1
            for r in range(n-1, -1, -1):
                if board[r][c] == 0:
                    continue
                if prev == 0:
                    new_board[cnt][c] = board[r][c]
                    cnt -= 1
                    prev = board[r][c]
                else:
                    if board[r][c] == prev:
                        new_board[cnt+1][c] *= 2
                        prev = 0
                    else:
                        new_board[cnt][c] = board[r][c]
                        prev = board[r][c]
                        cnt -= 1
            for i in range(cnt, -1, -1):
                new_board[i][c] = 0
    elif way == 'left':
        for r in range(n):
            prev = 0
            cnt = 0
            for c in range(n):
                if board[r][c] == 0:
                    continue
                if prev == 0:
                    new_board[r][cnt] = board[r][c]
                    cnt += 1
                    prev = board[r][c]
                else:
                    if board[r][c] == prev:
                        new_board[r][cnt-1] *= 2
                        prev = 0
                    else:
                        new_board[r][cnt] = board[r][c]
                        prev = board[r][c]
                        cnt += 1
            for i in range(cnt, n):
                new_board[r][i] = 0
    else:
        for r in range(n):
            prev = 0
            cnt = n-1
            for c in range(n-1, -1, -1):
                if board[r][c] == 0:
                    continue
                if prev == 0:
                    new_board[r][cnt] = board[r][c]
                    cnt -= 1
                    prev = board[r][c]
                else:
                    if board[r][c] == prev:
                        new_board[r][cnt+1] *= 2
                        prev = 0
                    else:
                        new_board[r][cnt] = board[r][c]
                        prev = board[r][c]
                        cnt -= 1
            for i in range(cnt, -1, -1):
                new_board[r][i] = 0
    return new_board

def dp(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(board[i]))
    else:
        dp(move(board, 'up'), cnt+1)
        dp(move(board, 'down'), cnt+1)
        dp(move(board, 'left'), cnt+1)
        dp(move(board, 'right'), cnt+1)

dp(board, 0)

print(ans)