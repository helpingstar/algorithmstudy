import sys

input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

board = []
zero_list = []
for r in range(9):
    line = list(map(int, input().rstrip()))
    for c, num in enumerate(line):
        if num == 0:
            zero_list.append((r, c))
    board.append(line)

def check(x, y, num):
    global board
    for r in range(9):
        if board[r][y] == num:
            return False
    for c in range(9):
        if board[x][c] == num:
            return False
        nx = x // 3 * 3
        ny = y // 3 * 3
    for r in range(3):
        for c in range(3):
            if board[nx+r][ny+c] == num:
                return False
    return True

def bt(cnt):
    global board
    # print(cnt)
    if cnt == len(zero_list):
        for line in board:
            print(*line, sep='')
        exit(0)

    x, y = zero_list[cnt]
    for i in range(1, 10):
        if check(x, y, i):
            board[x][y] = i
            bt(cnt+1)
            board[x][y] = 0

# print(len(zero_list))

bt(0)
