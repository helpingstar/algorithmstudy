import sys

input = sys.stdin.readline


def solution():
    ROW, COL = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(ROW)]
    target = [input().rstrip() for _ in range(ROW)]
    cnt = 0
    for r in range(ROW-2):
        for c in range(COL-2):
            if board[r][c] != target[r][c]:
                cnt += 1
                for dr in range(3):
                    for dc in range(3):
                        board[r+dr][c+dc] = '1' if board[r +
                                                         dr][c+dc] == '0' else '0'
        if (board[r][COL-2] != target[r][COL-2]) or (board[r][COL-1] != target[r][COL-1]):
            return -1
    for r in range(ROW-2, ROW):
        for c in range(COL):
            if board[r][c] != target[r][c]:
                return -1
    return cnt


print(solution())
