import sys

input = sys.stdin.readline
INF = int(1e7)
def strength(start, end):
    if start == 0:
        return 2
    if abs(start-end) % 2 == 1:
        return 3
    if abs(start-end) == 2:
        return 4
    if start == end:
        return 1

orders = list(map(int, input().split()))
orders

dp = [[[INF for _ in range(len(orders))] for _ in range(5)] for _ in range(5)]

dp[0][0][0] = 0

for i in range(len(orders)-1):
    for l in range(5):
        for r in range(5):
            if l != orders[i-1] and r != orders[i-1]:
                continue
            # print(f'[debug]  {i, l, r, orders[i]}')
            dp[l][orders[i]][i+1] = min(dp[l][orders[i]][i+1], dp[l][r][i] + strength(r, orders[i]))
            dp[orders[i]][r][i+1] = min(dp[orders[i]][r][i+1], dp[l][r][i] + strength(l, orders[i]))

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[l][r][len(orders)-1])

print(ans)