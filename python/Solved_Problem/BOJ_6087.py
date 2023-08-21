import sys
from collections import deque
input = sys.stdin.readline

def solution():
    INF = float('inf')
    COL, ROW = map(int, input().split())
    board = [input().rstrip() for _ in range(ROW)]
    mirrors = []
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == "C":
                mirrors.append((r, c))

    dist = [[[INF, INF, INF, INF] for _ in range(COL)] for _ in range(ROW)]
    sr, sc = mirrors[0]
    q = deque()
    for way in range(4):
        q.append((sr, sc, way, 0))
        dist[sr][sc][way] = 0

    while q:
        r, c, way, cnt = q.popleft()
        # print(r, c, way, cnt)

        if cnt > dist[r][c][way]:
            continue

        if way == 0:
            nr, nc = r - 1, c
        elif way == 1:
            nr, nc = r + 1, c
        elif way == 2:
            nr, nc = r, c - 1
        else:
            nr, nc = r, c + 1

        if (0 <= nr < ROW and 0 <= nc < COL) and dist[nr][nc][way] > dist[r][c][way] and not board[nr][nc] == "*":
            q.append((nr, nc, way, cnt))
            dist[nr][nc][way] = cnt

        if way in (0, 1):
            nc_list = [c - 1, c + 1]
            nr = r
            for nw, nc in enumerate(nc_list, 2):
                if (0 <= nr < ROW and 0 <= nc < COL) and dist[nr][nc][nw] > dist[r][c][way] + 1 and not board[nr][nc] == "*":
                    q.append((nr, nc, nw, cnt + 1))
                    dist[nr][nc][nw] = cnt + 1
        else:
            nr_list = [r - 1, r + 1]
            nc = c
            for nw, nr in enumerate(nr_list):
                if (0 <= nr < ROW and 0 <= nc < COL) and dist[nr][nc][nw] > dist[r][c][way] + 1 and not board[nr][nc] == "*":
                    q.append((nr, nc, nw, cnt + 1))
                    dist[nr][nc][nw] = cnt + 1

    er, ec = mirrors[1]
    print(min(dist[er][ec]))

solution()
