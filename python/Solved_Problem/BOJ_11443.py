import sys

input = sys.stdin.readline
MOD = 1000000007
n = int(input())

def fibo(n):
    def mul(mat1, mat2):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= MOD
        return result
    
    identity = [[1, 0], [0, 1]]
    multiplier = [[0, 1], [1, 1]]
    cnt = 0
    while n >= (1 << cnt):
        if n & (1 << cnt) != 0:
            identity = mul(identity, multiplier)
        cnt += 1
        multiplier = mul(multiplier, multiplier)
    
    return identity[0][1]

if n % 2 == 0:
    print(fibo(n+1)-1)
else:
    print(fibo(n)-1)