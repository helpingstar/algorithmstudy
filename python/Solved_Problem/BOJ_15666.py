n, m = map(int, input().split())

init_list = list(map(int, input().split()))
init_list.sort()
ans = set()

def dp(now, remain, count):
    if count == m:
        if tuple(now) not in ans:
            ans.add(tuple(now))
            print(*now)
        return
    for i in range(len(remain)):
        dp(now + [remain[i]],remain[i   :], count+1)

dp([], init_list, 0)
