from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for c in range(n):
            for r in range(n//2):
                matrix[r][c], matrix[n-1-r][c] = matrix[n-1-r][c], matrix[r][c]

        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
