import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def solution():
    n_edges, n_root, n_query = map(int, input().split())

    graph = [[] for _ in range(n_edges + 1)]

    for _ in range(n_edges - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    n_child = [0] * (n_edges + 1)

    def dp(now):
        n_child[now] = 1
        for nxt in graph[now]:
            if n_child[nxt] > 0:
                continue
            n_child[now] += dp(nxt)
        return n_child[now]

    dp(n_root)

    for _ in range(n_query):
        q = int(input())
        print(n_child[q])


solution()
