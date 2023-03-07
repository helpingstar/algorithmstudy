import sys
from collections import deque

input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def solution():
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    visited = [[[False, False] for _ in range(C)] for _ in range(R)]
    # print(visited)
    q = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == '*':
                q.appendleft((r, c, 1, 0))
                visited[r][c][1] = True
            elif board[r][c] == 'S':
                q.append((r, c, 0, 0))
                visited[r][c][0] = True
    while q:
        x, y, is_water, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if board[nx][ny] == 'X':
                continue

            if is_water:
                if board[nx][ny] == 'D':
                    continue
                if visited[nx][ny][1]:
                    continue
                board[nx][ny] = '*'
                visited[nx][ny][1] = True
                q.append((nx, ny, is_water, cnt+1))
            # 고슴도치
            else:
                if board[nx][ny] == 'D':
                    return cnt + 1
                if board[nx][ny] == '*':
                    continue
                if visited[nx][ny][0]:
                    continue
                board[nx][ny] = 'S'
                visited[nx][ny][0] = True
                q.append((nx, ny, is_water, cnt+1))
    return 'KAKTUS'


print(solution())
