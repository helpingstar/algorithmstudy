import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n_town = int(input())

population_list = [0] + list(map(int, input().split()))
visited = [False] * (n_town+1)
graph = [[] for _ in range(n_town+1)]
# 0: not good town 1: good town
table = [[0, population_list[i]] for i in range(n_town+1)]

for _ in range(n_town-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dp(now):
    visited[now] = True
    for next in graph[now]:
        if visited[next]:
            continue
        table[now][0] += max(dp(next))
        table[now][1] += dp(next)[0]
    return table[now]

print(max(dp(1)))
