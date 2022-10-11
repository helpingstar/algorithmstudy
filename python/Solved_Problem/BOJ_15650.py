n, m = map(int, input().split())

init_list = list(range(1, n+1))
ans = []

def dp(now, remain, count):
    if count == m:
        print(*now)
    for i in range(len(remain)):
        dp(now + [remain[i]],remain[i+1:], count+1)

dp([], init_list, 0)
