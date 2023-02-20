import sys

input = sys.stdin.readline

a, b = map(int, input().split())

MOD = 1_000_000_007

def fibo(x):
    def mul(mat1, mat2):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += mat1[i][k] * mat2[k][j]
                    result[i][j] %= MOD
                    
        return result
    cnt = 0
    identity = [[1, 0], [0, 1]]
    norm = [[0, 1], [1, 1]]
    while x >= (1 << cnt):
        if x & (1 << cnt) != 0:
            identity = mul(identity, norm)
        cnt += 1
        norm = mul(norm, norm)
    # print(identity)
    return identity[0][1]
    
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a -= b
        if a < b:
            a, b = b, a
    return b

print(fibo(gcd(a, b)))