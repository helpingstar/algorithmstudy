import sys
import bisect

input = sys.stdin.readline


def solution():
    N = int(input())
    prices = []
    for _ in range(N):
        graph = dict()
        line = input().rstrip()
        for i, x in enumerate(line):
            x = int(x)
            if x not in graph:
                graph[x] = [i]
            else:
                graph[x].append(i)
        prices.append(graph)

    visited = [False] * N
    visited[0] = True
    result = 1

    def dp(start, end, count, nprice):
        nonlocal prices, visited, N, result
        result = max(result, count)
        if result == N:
            return

        for i in

    for i in range(1, N):
        visited[i] = True
        dp(0, i, 2, 0)
        visited[i] = False

    print(result)


solution()
