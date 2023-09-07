import sys


def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    valid = [True] * (N + 1)
    result = 0
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dp(cnt, now):
        nonlocal result
        if cnt == 3:
            result += 1
            return

        for i in range(now, N + 1):
            if valid[i]:
                button = [n for n in graph[i] if valid[n]]
                for b in button:
                    valid[b] = False
                valid[i] = False
                dp(cnt + 1, i)
                for b in button:
                    valid[b] = True
                valid[i] = True

    dp(0, 1)
    print(result)


solution()
