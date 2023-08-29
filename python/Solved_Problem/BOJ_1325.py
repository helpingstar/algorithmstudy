import sys
from collections import deque


def solution():
    n_com, n_conn = map(int, input().split())

    graph = [[] for _ in range(n_com+1)]

    for _ in range(n_conn):
        a, b = map(int, input().split())
        graph[b].append(a)

    def bfs(start):
        nonlocal graph, n_com
        visited = [False] * (n_com + 1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if visited[nxt]:
                    continue
                cnt += 1
                q.append(nxt)
                visited[nxt] = True
        return cnt

    ans_list = []
    n_max = 0

    for i in range(1, n_com+1):
        temp = bfs(i)
        if temp == n_max:
            ans_list.append(i)
        elif temp > n_max:
            ans_list = [i]
            n_max = temp

    print(*ans_list)


solution()
