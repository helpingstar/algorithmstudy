import sys
from collections import deque

input = sys.stdin.readline


def solution():
    ROW, COL = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(ROW)]
    # 동, 서, 남, 북
    visited = [[[False, False, False, False] for _ in range(COL)] for _ in range(ROW)]
    t_right = (2, 3, 1, 0)
    t_left = (3, 2, 0, 1)
    delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # r, c, w
    a, b, c = list(map(int, input().split()))
    start = [a - 1, b - 1, c - 1]
    a, b, c = list(map(int, input().split()))
    end = (a - 1, b - 1, c - 1)

    if start[0] == end[0] and start[1] == end[1] and start[2] == end[2]:
        return 0

    visited[start[0]][start[1]][start[2]] = True
    q = deque()
    q.append(start + [0])
    while q:
        r, c, w, step = q.popleft()
        # forward
        dr, dc = delta[w]
        nr, nc = r + dr, c + dc
        for d in range(1, 4):
            nr = r + (dr * d)
            nc = c + (dc * d)
            if not (0 <= nr < ROW and 0 <= nc < COL):
                break
            if board[nr][nc] == 1:
                break
            if visited[nr][nc][w]:
                continue
            if (nr, nc, w) == end:
                return step + 1
            q.append((nr, nc, w, step + 1))
            # print(q[-1])
            visited[nr][nc][w] = True

        if (r, c, t_right[w]) == end or (r, c, t_left[w]) == end:
            return step + 1
        # turn right
        if not visited[r][c][t_right[w]]:
            q.append((r, c, t_right[w], step + 1))
            # print(q[-1])
            visited[r][c][t_right[w]] = True
        # turn left
        if not visited[r][c][t_left[w]]:
            q.append((r, c, t_left[w], step + 1))
            # print(q[-1])
            visited[r][c][t_left[w]] = True


print(solution())
