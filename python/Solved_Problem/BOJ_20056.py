import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    dr = (-1, -1, 0, 1, 1, 1, 0, -1)
    dc = (0, 1, 1, 1, 0, -1, -1, -1)
    size, n_ball, K = map(int, input().split())

    count = [[0] * size for _ in range(size)]
    higher_2 = set()

    def move(r, c, s, d):
        nr = (r + dr[d] * s) % size
        nc = (c + dc[d] * s) % size
        return nr, nc

    board = [[deque() for _ in range(size)] for _ in range(size)]
    for _ in range(n_ball):
        r, c, m, s, d = map(int, input().split())
        r -= 1
        c -= 1
        nr, nc = move(r, c, s, d)
        board[nr][nc].append((m, s, d))
        count[nr][nc] += 1
        if count[nr][nc] >= 2:
            higher_2.add((nr, nc))

    for r, c in higher_2:
        total_m = 0
        total_s = 0
        all_odd = True
        all_even = True
        for m, s, d in board[r][c]:
            total_m += m
            total_s += s
            if d % 2 == 0:
                all_odd = False
            else:
                all_even = False
        new_m = total_m // 5
        board[r][c] = deque()
        if new_m == 0:
            count[r][c] = 0
        else:
            new_s = total_s // count[r][c]
            if all_odd or all_even:
                delta = 0
            else:
                delta = 1
            board[r][c] = deque()
            for i in range(4):
                board[r][c].append((new_m, new_s, 2 * i + delta))
            count[r][c] = 4

    for _ in range(K-1):
        new_count = [[0] * size for _ in range(size)]
        higher_2 = set()
        for r in range(size):
            for c in range(size):
                if count[r][c] > 0:
                    for _ in range(count[r][c]):
                        m, s, d = board[r][c].popleft()
                        nr, nc = move(r, c, s, d)
                        board[nr][nc].append((m, s, d))
                        new_count[nr][nc] += 1
                        if new_count[nr][nc] >= 2:
                            higher_2.add((nr, nc))
        for r, c in higher_2:
            total_m = 0
            total_s = 0
            all_odd = True
            all_even = True
            for m, s, d in board[r][c]:
                total_m += m
                total_s += s
                if d % 2 == 0:
                    all_odd = False
                else:
                    all_even = False
            new_m = total_m // 5
            board[r][c] = deque()
            if new_m == 0:
                new_count[r][c] = 0
            else:
                new_s = total_s // new_count[r][c]
                if all_odd or all_even:
                    delta = 0
                else:
                    delta = 1
                board[r][c] = deque()
                for i in range(4):
                    board[r][c].append((new_m, new_s, 2 * i + delta))
                new_count[r][c] = 4
        count = new_count
    result = 0
    for r in range(size):
        for c in range(size):
            if count[r][c] > 0:
                for m, _, _ in board[r][c]:
                    result += m
    print(result)


solution()
