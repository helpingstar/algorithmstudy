import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
MOD = 1_000_000_007
cache = dict()

n, r = map(int, input().split())


def comb(n, r):
    if (n, r) in cache:
        return cache[(n, r)]
    if r == 0 or n - r == 0:
        cache[(n, r)] = 1
        return 1
    elif r == 1:
        cache[(n, r)] = n
        return n
    else:
        cache[(n, r)] = comb(n-1, r) + comb(n-1, r-1) % MOD
        return cache[(n, r)]


print(comb(n, r))
