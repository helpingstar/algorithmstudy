from collections import deque
import sys

input = sys.stdin.readline


def cheese(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                return True
    return False


def solution():
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    cnt = 0
    while True:
        if not cheese(board):
            return cnt
        cnt += 1
        visited = set()
        q = deque()
        visited.add((0, 0))
        q.append((0, 0))
        touch = dict()
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if (nr, nc) in visited:
                    continue
                if board[nr][nc] == 0:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                else:
                    if (nr, nc) not in touch:
                        touch[(nr, nc)] = 1
                    else:
                        touch[(nr, nc)] += 1
        for (r, c), t in touch.items():
            if t >= 2:
                board[r][c] = 0


print(solution())
