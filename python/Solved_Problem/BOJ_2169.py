"""
왼쪽에서 온 것은 다시 왼쪽으로 갈 수 없고
오른쪽에서 온 것은 다시 오른쪽으로 갈 수 없기 때문에
오른쪽에서 올 가능성이 있었던 것, 왼쪽에서 올 수 있었던 것을 나눈다..
[0] : 왼쪽에서 오거나 위에서온 것
[1] : 오른쪽에서 오거나 위에서 온 것

첫째줄, 마지막줄은 왼쪽에서 오른쪽으로밖에 못가기때문에 따로 처리한다.
첫째줄은 왼쪽에서부터 더해가고
마지막줄은 왼쪽 vs 위에것으로 하여 점점 구해간다.
"""


import sys

input = sys.stdin.readline

INF = -sys.maxsize
r, c = map(int, input().split())

board = []

for _ in range(r):
    board.append(list(map(int, input().split())))

matrix = []

for _ in range(r):
    matrix.append([[INF, INF] for _ in range(c)])

matrix[0][0][0] = board[0][0]
matrix[0][0][1] = board[0][0]

for i in range(1, c):
    matrix[0][i][0] = matrix[0][i-1][0] + board[0][i]
    matrix[0][i][1] = matrix[0][i-1][1] + board[0][i]

for i in range(1, r-1):
    matrix[i][0][0] = max(matrix[i-1][0]) + board[i][0]
    for j in range(1, c):
        matrix[i][j][0] = max(matrix[i][j-1][0], max(matrix[i-1][j])) + board[i][j]
    
    matrix[i][c-1][1] = max(matrix[i-1][c-1]) + board[i][c-1]
    for j in range(c-2, -1, -1):
        matrix[i][j][1] = max(matrix[i][j+1][1], max(matrix[i-1][j])) + board[i][j]

if r == 1:
    print(matrix[r-1][c-1][0])
else:
    matrix[r-1][0][0] = max(matrix[r-2][0]) + board[r-1][0]

    for i in range(1, c):
        matrix[r-1][i][0] = max(matrix[r-1][i-1][0], max(matrix[r-2][i])) + board[r-1][i]

    print(matrix[r-1][c-1][0])
    