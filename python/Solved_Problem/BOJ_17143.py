import sys

input = sys.stdin.readline

# 1 : 위 / 2 : 아래 / 3 : 오른쪽 / 4 : 왼쪽


def move(R, C, s, d, r, c):
    if d == 1 or d == 2:
        if 0 < r < (R - 1):
            if d == 1:
                start = 2 * (R - 1) - r
            else:
                start = r
        else:
            start = r
        end = (start + s) % ((R - 1) * 2)

        if end == 0 or end == (R - 1):
            return (end, c, 1)
        elif 0 < end < (R-1):
            return (end, c, 2)
        else:
            return (2 * (R - 1) - end, c, 1)
    else:
        if 0 < c < (C-1):
            if d == 4:
                start = 2 * (C-1) - c
            else:
                start = c
        else:
            start = c
        end = (start + s) % ((C - 1) * 2)

        if end == 0 or end == (C-1):
            return (r, end, 3)
        elif 0 < end < (C-1):
            return (r, end, 3)
        else:
            return (r, 2 * (C - 1) - end, 4)


def solution():
    R, C, M = map(int, input().split())
    board = [[None] * C for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        r -= 1
        c -= 1
        board[r][c] = [s, d, z]

    result = 0
    for c in range(C):
        for r in range(R):
            if board[r][c]:
                result += board[r][c][2]
                board[r][c] = None
                break
        new_board = [[None] * C for _ in range(R)]

        for x in range(R):
            for y in range(C):
                if board[x][y]:
                    s, d, z = board[x][y]
                    nx, ny, nd = move(R, C, s, d, x, y)
                    if new_board[nx][ny]:
                        if new_board[nx][ny][2]:
                            if new_board[nx][ny][2] < z:
                                new_board[nx][ny] = [s, nd, z]
                    else:
                        new_board[nx][ny] = [s, nd, z]
        board = new_board
        # print('='*20)
        # for line in board:
        #     print(line)
        # print('='*20)
    return result


print(solution())
