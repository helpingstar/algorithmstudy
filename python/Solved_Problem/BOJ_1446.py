import sys

input = sys.stdin.readline


def solution():
    N, D = map(int, input().split())
    fast = []
    for _ in range(N):
        s, e, dist = map(int, input().split())
        if e <= D:
            fast.append((s, e, dist))
    dp = [i for i in range(D+1)]
    fast.sort(key=lambda x: x[1])

    for s, e, dist in fast:
        if dp[e] > dp[s] + dist:
            dp[e] = dp[s] + dist
            for i in range(e+1, D+1):
                dp[i] = min(dp[i], dp[i-1] + 1)
    print(dp[D])


solution()
