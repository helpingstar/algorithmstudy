import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    parents = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for i, p in enumerate(parents[1:], 1):
        graph[p].append(i)

    def dp(now):
        nonlocal parents, graph
        if len(graph[now]) == 0:
            return 0
        times = []
        for nxt in graph[now]:
            times.append(dp(nxt))
        times.sort(reverse=True)
        turntimes = []
        for i in range(len(graph[now])):
            turntimes.append(i+1+times[i])
        return max(turntimes)

    print(dp(0))


solution()
