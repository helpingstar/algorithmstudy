from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
early = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dp(now):
    visited[now] = True

    for next in graph[now]:
        if visited[next]:
            continue
        dp(next)
        # 얼리어답터 아님
        early[now][0] += early[next][1]
        # 얼리어답터임
        early[now][1] += min(early[next])

    early[now][1] += 1

dp(1)
print(min(early[1]))