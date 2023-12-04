import sys

input = sys.stdin.readline


def solution():
    n_row, n_col, n_magic = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n_row)]

    five = ((0, n_col // 2), (n_row // 2, 0), (-n_row // 2, 0), (0, -n_col // 2))
    six = (five[1], five[3], five[0], five[2])

    fs = [five, six]

    def operator(op):
        nonlocal board, n_row, n_col

        if op == 1:
            for r in range(n_row // 2):
                board[r], board[n_row - 1 - r] = board[n_row - 1 - r], board[r]
        elif op == 2:
            for r in range(n_row):
                board[r] = board[r][::-1]
        elif op == 3:
            new_board = [[0] * n_row for _ in range(n_col)]
            for r in range(n_row):
                for c in range(n_col):
                    new_board[c][n_row - 1 - r] = board[r][c]
            board = new_board
            n_row, n_col = n_col, n_row
        elif op == 4:
            new_board = [[0] * n_row for _ in range(n_col)]
            for r in range(n_row):
                for c in range(n_col):
                    new_board[n_col - 1 - c][r] = board[r][c]
            board = new_board
            n_row, n_col = n_col, n_row
        else:
            if op == 5:
                delta = ((0, n_col // 2), (n_row // 2, 0), (-n_row // 2, 0), (0, -n_col // 2))
            else:
                delta = ((n_row // 2, 0), (0, -n_col // 2), (0, n_col // 2), (-n_row // 2, 0))
            new_board = [[0] * n_col for _ in range(n_row)]
            # 1
            for r in range(n_row // 2):
                c = 0
                nr = r + delta[0][0]
                nc = c + delta[0][1]
                new_board[nr][nc:nc+n_col // 2] = board[r][c:c+n_col // 2]
            # 2
            for r in range(n_row // 2):
                c = n_col // 2
                nr = r + delta[1][0]
                nc = c + delta[1][1]
                new_board[nr][nc:nc+n_col // 2] = board[r][c:c+n_col // 2]
            # 3
            for r in range(n_row // 2, n_row):
                c = 0
                nr = r + delta[2][0]
                nc = c + delta[2][1]
                new_board[nr][nc:nc+n_col // 2] = board[r][c:c+n_col // 2]
            # 4
            for r in range(n_row // 2, n_row):
                c = n_col // 2
                nr = r + delta[3][0]
                nc = c + delta[3][1]
                new_board[nr][nc:nc+n_col // 2] = board[r][c:c+n_col // 2]
            board = new_board

    for n in list(map(int, input().split())):
        operator(n)
    
    for line in board:
        print(*line)

solution()