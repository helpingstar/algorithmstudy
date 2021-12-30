import sys

T = int(sys.stdin.readline())

for _ in range(T):
    # row : N, x / col : M, y
    col, row, K = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(row):
        matrix.append([0] * col)

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1

    def dfs(x, y):
        if 0 <= x < row and 0 <= y < col:
            if matrix[x][y] == 0:
                return False
            matrix[x][y] = 0

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
    count = 0
    for i in range(row):
        for j in range(col):
            if dfs(i, j):
                count += 1
            
    print(count)