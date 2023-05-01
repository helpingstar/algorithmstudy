import sys
input = sys.stdin.readline

N = int(input())

MOD = 1000000007

def check(n, s):
    result = 1

    cursor = n
    cnt = 0

    while (1 << cnt) <= (MOD-2):
        if (1 << cnt) & (MOD-2) != 0:
            result *= cursor
            result % MOD

        cursor = cursor * cursor % MOD
        cnt += 1

    result = (result * s) % MOD
    return result

ans = 0

for _ in range(N):
    n, s = map(int, input().split())
    ans += check(n, s)
    ans %= MOD
print(ans)
