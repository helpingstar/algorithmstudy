class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])

        for r in range(N):
            for c in range(N):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(N):
            for i in range(N // 2):
                matrix[r][i], matrix[r][N-1-i] = matrix[r][N-1-i], matrix[r][i]
