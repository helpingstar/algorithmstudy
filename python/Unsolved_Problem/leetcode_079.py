from typing import List
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(row, col, word):
            if not word:
                return True
            origin = board[row][col]
            board[row][col] = '#'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            for r, c in (
                    (row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if (0 <= r < R and 0 <= c < C and
                        board[r][c] == word[0] and dfs(r, c, word[1:])):
                    return True
            board[row][col] = origin

        for row in range(R):
            for col in range(C):
                if (board[row][col] == word[0] and
                        dfs(row, col, word[1:])):
                    return True
        return False


board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
a = Solution()
print(a.exist(board, word))
