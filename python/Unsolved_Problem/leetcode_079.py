from typing import List
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]
        n_row = len(board)
        n_col = len(board[0])
        q = deque()
        check = set()
        for r, line in enumerate(board):
            for c, char in enumerate(line):
                if char == start:
                    q.append((r, c, 1, [(r, c)]))
        if len(word) == 1 and q:
            return True
        while q:
            x, y, pos, arr = q.popleft()
            print(pos)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n_row and 0 <= ny < n_col):
                    continue

                new_arr = arr + [(nx, ny)]
                new_tuple = tuple(sorted(new_arr))

                if new_tuple in check:
                    continue
                if board[nx][ny] == word[pos]:
                    if pos+1 == len(word):
                        return True
                    q.append((nx, ny, pos+1, new_arr))
                    check.add(new_tuple)
        return False


board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
a = Solution()
print(a.exist(board, word))
