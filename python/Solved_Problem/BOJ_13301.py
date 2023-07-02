import sys

input = sys.stdin.readline

def fibo(n):
    def mul(mat1, mat2):
        result = [[0, 0], [0, 0]]
        for r in range(2):
            for c in range(2):
                for k in range(2):
                    result[r][c] += mat1[r][k] * mat2[k][c]
        return result
    
    identity = [[1, 0], [0, 1]]
    temp = [[0, 1], [1, 1]]
    
    cnt = 0
    while n >= (1 << cnt):
        if n & (1 << cnt) != 0:
            identity = mul(identity, temp)
        cnt += 1
        temp = mul(temp, temp)
    
    return identity[0][1]

n = int(input())
print(fibo(n) * 4 + fibo(n-1) * 2)