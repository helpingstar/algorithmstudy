n, m = map(int, input().split())

init_list = list(range(1, n+1))
ans = []

def dp(now, remain, count):
    if count == m:
        print(*now)
    else:
        for i in range(n):
            dp(now + [remain[i]], remain, count+1)

dp([], init_list, 0)
