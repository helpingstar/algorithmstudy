import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def solution():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    colors = [0] * (V+1)
    visited = [False] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    for i in range(1, V+1):
        if visited[i]:
            continue
        q.append((i, 1))
        colors[i] = 1
        while q:
            now, c = q.popleft()
            for nxt in graph[now]:
                if visited[nxt]:
                    continue
                if colors[nxt] == 0:
                    colors[nxt] = -1 * c
                else:
                    if colors[nxt] == c:
                        return False
                q.append((nxt, -1*c))
            visited[now] = True
        # print(colors)
    return True


for _ in range(T):
    if solution():
        print('YES')
    else:
        print('NO')
