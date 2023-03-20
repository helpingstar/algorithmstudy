import sys

MOD = 10007

N, K = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result % MOD

def square(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a

    temp = square(a, b//2)

    if b % 2 == 0:
        return temp * temp % MOD
    else:
        return temp * temp * a % MOD

x = factorial(N)
y = factorial(K)
z = factorial(N-K)

yz = square(y*z, MOD-2)

print((x * yz) % MOD)
