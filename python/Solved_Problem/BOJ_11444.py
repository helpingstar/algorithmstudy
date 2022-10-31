import sys

input = sys.stdin.readline

num = int(input())

def fibo(n):
    f = [[1, 1], [1, 0]]
    identity = [[1, 0], [0, 1]]
    def mul(a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for n in range(2):
                    result[i][j] += a[i][n] * b[n][j]
                    result[i][j] %= 1000000007
        return result
    shift = 0
    while n >= (1 << shift):
        if n & (1 << shift) != 0:
            identity = mul(identity, f)
        f = mul(f, f)
        shift += 1
    return identity[0][1]

print(fibo(num))
