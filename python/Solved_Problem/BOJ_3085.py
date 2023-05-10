import sys

input = sys.stdin.readline

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]


def check():
    max_line = 1
    for r in range(N):
        temp = 1
        for c in range(N-1):
            if board[r][c] == board[r][c+1]:
                temp += 1
            else:
                max_line = max(max_line, temp)
                temp = 1
        max_line = max(max_line, temp)

    for c in range(N):
        temp = 1
        for r in range(N-1):
            if board[r][c] == board[r+1][c]:
                temp += 1
            else:
                max_line = max(max_line, temp)
                temp = 1
        max_line = max(max_line, temp)

    return max_line


ans = 1

for r in range(N):
    for c in range(N):
        if r+1 < N:
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
            ans = max(ans, check())
            board[r+1][c], board[r][c] = board[r][c], board[r+1][c]

        if c+1 < N:
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
            ans = max(ans, check())
            board[r][c+1], board[r][c] = board[r][c], board[r][c+1]

print(ans)
