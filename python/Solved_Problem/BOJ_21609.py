import sys
from collections import deque

input = sys.stdin.readline


def solution():
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    score = 0
    # -2 : blank, -1 : black, 0 : rainbow, 1~ : color
    n_size, n_color = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n_size)]
    visited = [[0] * n_size for _ in range(n_size)]
    # def print_board():
    #     print('-'*10)
    #     for line in board:
    #         print(line)
    #     print('-'*10)
    def bfs(r, c, cnt):
        color = board[r][c]
        rainbow_visit = set()
        block_group = [(r, c)]
        island_size = 1
        q = deque()
        q.append((r, c))
        visited[r][c] = cnt
        while q:
            r, c = q.popleft()
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < n_size and 0 <= nc < n_size):
                    continue
                if board[nr][nc] <= -1:
                    continue
                # rainbow
                if board[nr][nc] == 0:
                    if (nr, nc) in rainbow_visit:
                        continue
                    rainbow_visit.add((nr, nc))
                # color
                elif board[nr][nc] != color:
                    continue
                else:
                    if visited[nr][nc] == cnt:
                        continue
                    visited[nr][nc] = cnt
                island_size += 1
                q.append((nr, nc))
                block_group.append((nr, nc))
        return island_size, len(rainbow_visit), block_group

    def gravity():
        nxt_board = [[-2] * n_size for _ in range(n_size)]
        for c in range(n_size):
            cur = n_size - 1
            for r in range(n_size - 1, -1, -1):
                if board[r][c] == -2:
                    continue
                elif board[r][c] == -1:
                    cur = r - 1
                    nxt_board[r][c] = -1
                else:
                    nxt_board[cur][c] = board[r][c]
                    cur -= 1
        return nxt_board

    def counter_clockwise():
        nxt_board = [[-2] * n_size for _ in range(n_size)]
        for r in range(n_size):
            for c in range(n_size):
                nxt_board[n_size - 1 - c][r] = board[r][c]
        return nxt_board

    cnt = 1
    while True:
        candidate = (2, 0, -1, -1)
        cand_group = []
        for r in range(n_size):
            for c in range(n_size):
                if board[r][c] <= 0:
                    continue
                if visited[r][c] == cnt:
                    continue
                result, rainbow_cnt, block_group = bfs(r, c, cnt)
                if result >= 2:
                    nxt_candidate = max(candidate, (result, rainbow_cnt, r, c))
                    if nxt_candidate != candidate:
                        candidate = nxt_candidate
                        cand_group = block_group

        if candidate[2] == -1:
            break
        score += len(cand_group) ** 2

        for r, c in cand_group:
            board[r][c] = -2

        board = gravity()
        board = counter_clockwise()
        board = gravity()
        cnt += 1
    print(score)

solution()