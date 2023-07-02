import sys
from collections import deque


def solve():
    input = sys.stdin.readline
    R, C = map(int, input().split())

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    board = [list(input().rstrip()) for _ in range(R)]

    j_list = deque()
    f_list = deque()

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'J':
                j_list.append((r, c))
            if board[r][c] == 'F':
                f_list.append((r, c))

    cnt = 0
    while True:
        cnt += 1

        jn_list = deque()
        fn_list = deque()

        if not j_list:
            return 'IMPOSSIBLE'
        while j_list:
            jx, jy = j_list.popleft()
            if board[jx][jy] == 'F':
                continue
            for i in range(4):
                jnx = jx + dx[i]
                jny = jy + dy[i]
                if not (0 <= jnx < R and 0 <= jny < C):
                    return cnt
                if board[jnx][jny] in {'F', '#', 'J'}:
                    continue
                board[jnx][jny] = 'J'
                jn_list.append((jnx, jny))

        j_list = jn_list

        while f_list:
            fx, fy = f_list.popleft()
            for i in range(4):
                fnx = fx + dx[i]
                fny = fy + dy[i]
                if not (0 <= fnx < R and 0 <= fny < C):
                    continue
                if board[fnx][fny] in {'F', '#'}:
                    continue
                board[fnx][fny] = 'F'
                fn_list.append((fnx, fny))

        f_list = fn_list


if __name__ == "__main__":
    print(solve())
