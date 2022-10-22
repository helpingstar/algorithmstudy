import sys

input = sys.stdin.readline

n = int(input())

def fibo(n):
    f = [[1, 1], [1, 0]]
    identity = [[1, 0], [0, 1]]

    def mul(a, b, size):
        ans = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for n in range(size):
                    ans[i][j] += (a[i][n] * b[n][j])
                    ans[i][j] %= 1_000_000_007
        return ans

    if n == 0:
        return 0
    elif n == 1:
        return 1

    k = 0
    while n >= (1 << k):
        if n & (1 << k) != 0:
            identity = mul(identity, f, 2)
        f = mul(f, f, 2)
        k += 1

    return identity[0][1]


print(fibo(n))
