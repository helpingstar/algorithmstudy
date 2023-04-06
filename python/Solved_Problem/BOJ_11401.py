import sys

input = sys.stdin.readline

MOD = 1000000007


def fac(n):
    result = 1

    for i in range(2, n+1):
        result *= i
        result %= MOD

    return result


def square(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    temp = square(a, b//2)
    if b % 2 == 0:
        return (temp * temp) % MOD
    else:
        return (temp * temp * a) % MOD


n, k = map(int, input().split())

left = fac(n)
right = fac(k) * fac(n-k) % MOD
right = square(right, MOD-2)

print(left * right % MOD)
