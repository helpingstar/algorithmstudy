import sys

sys.setrecursionlimit(10**6)

def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    visited = [False] * (N+1)
    hacking = [1] * (N + 1)

    def dfs(now):
        if visited[now]:
            return hacking[now]
        visited[now] = True
        result = 1
        for nxt in graph[now]:
            result += dfs(nxt)
        hacking[now] = result
        return result

    for i in range(1, N+1):
        dfs(i)

    n_max = 0
    ans = []
    for i in range(1, N+1):
        if hacking[i] > n_max:
            n_max = hacking[i]
            ans = [i]
        elif hacking[i] == n_max:
            ans.append(i)
    print(*sorted(ans))

solution()
