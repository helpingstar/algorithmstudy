from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_row, n_col = len(matrix), len(matrix[0]) 
        print(f'debug {n_row}, {n_col}')
        row_zero = [False] * n_row
        col_zero = [False] * n_col
        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] == 0:
                    row_zero[r] = True
                    col_zero[c] = True
        print(row_zero)
        print(col_zero)
        for r in range(n_row):
            for c in range(n_col):
                if row_zero[r] or col_zero[c]:
                    matrix[r][c] = 0
        print(matrix)
                

matrix = [[1,1,1],[1,0,1],[1,1,1]]
a = Solution()

a.setZeroes(matrix)