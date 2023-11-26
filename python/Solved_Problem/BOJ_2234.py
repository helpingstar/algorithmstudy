import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n_col, n_row = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n_row)]
    visited = [[False] * n_col for _ in range(n_row)]
    region = [[-1] * n_col for _ in range(n_row)]
    size_list = []

    # L, U, R, D
    way = (1, 2, 4, 8)
    move = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def bfs(r, c, cnt):
        size = 1
        q = deque()
        q.append((r, c))
        visited[r][c] = True
        while q:
            r, c = q.popleft()
            region[r][c] = cnt
            for i in range(4):
                if board[r][c] & way[i] == 0:
                    nr = r + move[i][0]
                    nc = c + move[i][1]
                    if not (0 <= nr < n_row and 0 <= nc < n_col):
                        continue
                    if visited[nr][nc]:
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    size += 1
        return size

    cnt = 0
    for r in range(n_row):
        for c in range(n_col):
            if visited[r][c]:
                continue
            size = bfs(r, c, cnt)
            size_list.append(size)
            cnt += 1


    conn_set = set()

    for r in range(n_row):
        for c in range(n_col):
            for dr, dc, in move:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < n_row and 0 <= nc < n_col):
                    continue
                if region[r][c] != region[nr][nc]:
                    conn_set.add((min(region[r][c], region[nr][nc]), max(region[r][c], region[nr][nc])))

    conn_result = 0
    for a, b in conn_set:
        conn_result = max(conn_result, size_list[a] + size_list[b])

    print(len(size_list))
    print(max(size_list ))
    print(conn_result)

solution()
