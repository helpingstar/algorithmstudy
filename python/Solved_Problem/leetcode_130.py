from collections import deque
from typing import *

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        n_col = len(board[0])

        visited = [[False] * n_col for _ in range(n_row)]

        def bfs(x, y):
            memory = []
            visited[x][y] = True
            stick_to_wall = False
            q = deque()
            q.append((x, y))
            memory.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < n_row and 0 <= ny < n_col):
                        stick_to_wall = True
                        continue
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] == "X":
                        continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    memory.append((nx, ny))
            if not stick_to_wall:
                for x, y in memory:
                    board[x][y] = "X"

        for r in range(n_row):
            for c in range(n_col):
                if board[r][c] == "O":
                    if visited[r][c]:
                        continue
                    bfs(r, c)
