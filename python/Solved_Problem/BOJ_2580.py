import sys

input = sys.stdin.readline

zero_list = []
board = [list(map(int, input().split())) for _ in range(9)]

col_list = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
row_list = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
blk_list = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zero_list.append((r, c))
        else:
            col_list[c].remove(board[r][c])
            row_list[r].remove(board[r][c])
            blk_list[r//3 * 3 + c//3].remove(board[r][c])

def check_col(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

def check_row(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

def check_box(r, c, num):
    r //= 3
    r *= 3
    c //= 3
    c *= 3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] == num:
                return False
    return True

def bt(idx):
    if idx == len(zero_list):
        for line in board:
            print(*line)
        exit(0)
    r, c = zero_list[idx]
    for num in col_list[c] & row_list[r] & blk_list[r//3 * 3 + c//3]:
        if check_col(c, num) and check_row(r, num) and check_box(r, c, num):
            board[r][c] = num
            bt(idx+1)
            board[r][c] = 0

bt(0)
