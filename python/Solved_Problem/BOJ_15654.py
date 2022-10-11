n, m = map(int, input().split())

init_list = list(map(int, input().split()))
init_list.sort()

def dp(now, remain, count):
    if count == m:
        print(*now)
        return
    for i in range(len(remain)):
        dp(now + [remain[i]], remain[:i] + remain[i+1:], count+1)

dp([], init_list, 0)
