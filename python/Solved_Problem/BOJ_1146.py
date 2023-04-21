import sys

input = sys.stdin.readline

N = int(input())

MOD = 1000000

cache = [[0] * (N+1) for _ in range(N+1)]

def dp(left, right):
    if left + right == 0:
        return 1

    if right == 0:
        return 0

    if cache[left][right]:
        return cache[left][right]

    for i in range(right):
        cache[left][right] += dp(right - i - 1, left + i)
        cache[left][right] %= MOD
    return cache[left][right]

answer = 0
if N == 1:
    answer = 1
else:
    answer += dp(0, N) * 2
print(answer % MOD)
