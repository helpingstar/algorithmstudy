import sys

input = sys.stdin.readline
MOD = 1000000000
a, b = map(int, input().split())

def fibo(n):
    def mul(mat1, mat2):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= MOD
        return result
    
    multiplier = [[0, 1], [1, 1]]
    identity = [[1, 0], [0, 1]]
    
    cnt = 0
    while n >= (1 << cnt):
        if n & (1 << cnt) != 0:
            identity = mul(identity, multiplier)
        multiplier = mul(multiplier, multiplier)
        cnt += 1
    return identity[0][1]

print((fibo(b + 2) - fibo(a + 1)) % MOD)