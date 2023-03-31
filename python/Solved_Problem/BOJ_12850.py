import sys

input = sys.stdin.readline
MOD = 1000000007
n = int(input())

matrix = [
    #  0  1  2  3  4  5  6  7
    [0, 1, 0, 1, 0, 0, 0, 0],  # 0
    [1, 0, 1, 1, 0, 0, 0, 0],  # 1
    [0, 1, 0, 1, 1, 1, 0, 0],  # 2
    [1, 1, 1, 0, 0, 1, 0, 0],  # 3
    [0, 0, 1, 0, 0, 1, 1, 0],  # 4
    [0, 0, 1, 1, 1, 0, 0, 1],  # 5
    [0, 0, 0, 0, 1, 0, 0, 1],  # 6
    [0, 0, 0, 0, 0, 1, 1, 0]  # 7
]

identity = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]


def multiply(mat1, mat2):
    temp = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                temp[i][j] += mat1[i][k] * mat2[k][j]
                temp[i][j] %= MOD
    return temp


cnt = 0

while n >= (1 << cnt):
    if n & (1 << cnt) != 0:
        identity = multiply(identity, matrix)

    matrix = multiply(matrix, matrix)

    cnt += 1

print(identity[0][0])
