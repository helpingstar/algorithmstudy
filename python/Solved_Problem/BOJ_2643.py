import sys
import bisect

input = sys.stdin.readline
INF = 1001
n_paper = int(input())
dp = [INF] * (n_paper + 1)
papers = []
for _ in range(n_paper):
    a, b = map(int, input().split())
    if a > b:
        papers.append((b, a))
    else:
        papers.append((a, b))

papers.sort(key=lambda x: (x[-1], x[0]))
ans = 0

for l, h in papers:
    pos = bisect.bisect_right(dp, l)
    dp[pos] = l
    ans = max(ans, pos)

print(ans+1)
