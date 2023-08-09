import sys
from collections import deque

input = sys.stdin.readline


def solution():
    ROW, COL = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(ROW)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    visited = [[0] * COL for _ in range(ROW)]

    def bfs(x, y, v):
        nonlocal board, dx, dy, visited
        q = deque([(x, y, 0)])
        visited[x][y] += 1
        while q:
            x, y, dist = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < ROW and 0 <= ny < COL):
                    continue
                if board[nx][ny] == "W":
                    continue
                if visited[nx][ny] == v:
                    continue

                visited[nx][ny] += 1
                q.append((nx, ny, dist + 1))
        return dist

    result = 0
    for x in range(ROW):
        for y in range(COL):
            if board[x][y] == "L":
                result = max(result, bfs(x, y, visited[x][y]+1))
    print(result)


solution()
