import sys
from collections import deque

input = sys.stdin.readline


def solution():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    ROW, COL = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(ROW)]
    distance = [[-1] * COL for _ in range(ROW)]

    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 2:
                sr, sc = r, c
                distance[sr][sc] = 0
            elif board[r][c] == 0:
                distance[r][c] = 0
    q = deque()
    q.append((sr, sc, 0))
    while q:
        r, c, dist = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < ROW and 0 <= nc < COL):
                continue
            if distance[nr][nc] == -1:
                distance[nr][nc] = dist + 1
                q.append((nr, nc, dist+1))

    for line in distance:
        print(*line)


solution()
