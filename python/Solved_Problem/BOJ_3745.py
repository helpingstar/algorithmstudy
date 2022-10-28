import sys
import bisect

input = sys.stdin.readline
INF = 100001

def solution():
    n = int(input())
    if n == 1:
        return 1
    ans = 0
    arr = list(map(int, input().split()))
    dp = [0] + [INF for _ in range(n)]
    for idx, num in enumerate(arr, start=1):
        pos = bisect.bisect_left(dp, num)
        dp[pos] = num
        ans = max(pos, ans)
    return ans



while True:
    try:
        print(solution())
    except:
        break
