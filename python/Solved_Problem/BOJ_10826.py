import sys

input = sys.stdin.readline


def fibo(n):
    identity = [[1, 0], [0, 1]]
    cursor = [[0, 1], [1, 1]]

    def mul(mat1, mat2):
        temp = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    temp[i][j] += mat1[i][k] * mat2[k][j]
        return temp

    cnt = 0
    while n >= (1 << cnt):
        if n & (1 << cnt) != 0:
            identity = mul(identity, cursor)
        cursor = mul(cursor, cursor)
        cnt += 1
    return identity[0][1]

print(fibo(int(input())))
