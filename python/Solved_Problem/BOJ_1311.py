import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    cache = [[0] * (1 << N) for _ in range(N)]

    def dp(now, visited):
        nonlocal cache
        if now == N:
            return 0

        if cache[now][visited] != 0:
            return cache[now][visited]

        temp = float('inf')
        for idx in range(N):
            if visited & (1 << idx) > 0:
                continue

            temp = min(temp, cost[now][idx] + dp(now+1, visited | (1 << idx)))
        cache[now][visited] = temp
        return cache[now][visited]

    # ans = float('inf')
    # for i in range(N):
    #     ans = min(ans, dp(0, 0))
    # print(ans)
    print(dp(0, 0))


solution()
