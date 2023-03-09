from itertools import combinations
import sys

input = sys.stdin.readline


def check(board, R, C):
    for c in range(C):
        cur = c
        for r in range(R):
            if board[r][cur] == 1:
                cur += 1
            elif board[r][cur] == 2:
                cur -= 1
        if cur != c:
            return False
    return True


def solution():
    C, n, R = map(int, input().split())

    # 0: none / 1: -> / 2 : <-
    board = [[0] * C for _ in range(R)]

    for _ in range(n):
        a, b = map(int, input().split())
        board[a-1][b-1] = 1
        board[a-1][b] = 2

    # for i in board:
        # print(i)

    available = []
    for r in range(R):
        for c in range(C-1):
            if board[r][c] == 0 and board[r][c+1] == 0:
                available.append((r, c))

    for i in range(4):
        for combis in combinations(available, i):
            # print(i)
            for x, y in combis:
                board[x][y] = 1
                board[x][y+1] = 2
            if check(board, R, C):
                return i
            for x, y in combis:
                board[x][y] = 0
                board[x][y+1] = 0

    return -1


print(solution())
