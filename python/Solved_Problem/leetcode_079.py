from typing import *

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n_row = len(board)
        n_col = len(board[0])
        def dfs(x, y, count):
            if count == len(word):
                return True
            if board[x][y] != word[count]:
                return False
            if not (0 <= x < n_row and 0 <= y < n_col):
                return False
            if (x, y) in visited:
                return False

            visited.add((x, y))

            ans = (dfs(x+1, y, count+1) or dfs(x-1, y, count+1) or
                    dfs(x, y+1, count+1) or dfs(x, y-1, count+1))
            visited.remove((x, y))
            return ans

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
