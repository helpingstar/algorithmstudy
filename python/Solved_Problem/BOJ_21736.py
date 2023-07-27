import sys
from collections import deque

input = sys.stdin.readline


def solution():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    ROW, COL = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(ROW)]
    visited = [[False] * COL for _ in range(ROW)]
    for r, line in enumerate(board):
        if "I" in line:
            sr, sc = r, line.index("I")
            break

    cnt = 0
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < ROW and 0 <= nc < COL):
                continue
            if board[nr][nc] == "X":
                continue
            if visited[nr][nc]:
                continue

            if board[nr][nc] == 'P':
                cnt += 1
            q.append((nr, nc))
            visited[nr][nc] = True

    result = "TT" if cnt == 0 else cnt
    return result


print(solution())
