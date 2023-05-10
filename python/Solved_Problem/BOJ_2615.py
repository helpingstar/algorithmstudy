import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

visited = [[[False, False, False, False]
            for i in range(19)] for j in range(19)]

# 0: -, 1: |, 2: \


def check(r, c):
    # -
    cursor = 0
    while (c + cursor < 19) \
            and (board[r][c] == board[r][c+cursor]) \
            and (not visited[r][c+cursor][0]):
        visited[r][c+cursor][0] = True
        cursor += 1
    if cursor == 5:
        return board[r][c], r, c

    # |
    cursor = 0
    while (r + cursor < 19) \
            and (board[r][c] == board[r+cursor][c]) \
            and (not visited[r+cursor][c][1]):
        visited[r+cursor][c][1] = True
        cursor += 1
    if cursor == 5:
        return board[r][c], r, c

    # \
    cursor = 0
    while (r + cursor < 19) \
            and (c + cursor < 19) \
            and (board[r][c] == board[r+cursor][c+cursor]) \
            and (not visited[r+cursor][c+cursor][2]):
        visited[r+cursor][c+cursor][2] = True
        cursor += 1
    if cursor == 5:
        return board[r][c], r, c

    # /
    cursor = 0
    while (r + cursor < 19) \
            and (c - cursor >= 0) \
            and (board[r][c] == board[r+cursor][c-cursor]) \
            and (not visited[r+cursor][c-cursor][3]):
        visited[r+cursor][c-cursor][3] = True
        cursor += 1
    if cursor == 5:
        return board[r][c], r+4, c-4

    return 0, 0, 0


def solution():
    for r in range(19):
        for c in range(19):
            if board[r][c] == 0:
                continue
            if visited[r][c][0] and visited[r][c][1] and visited[r][c][2] and visited[r][c][3]:
                continue
            win, x, y = check(r, c)
            if win != 0:
                print(win)
                print(x+1, y+1)
                return
    print(0)


solution()

# print(visited)
