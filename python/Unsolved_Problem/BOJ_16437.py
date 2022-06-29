import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
info = {}
graph = [[] for _ in range(n+1)]


for i in range(2, n+1):
    sw, popu, edge = input().rstrip().split()
    popu, edge = int(popu), int(edge)

    graph[edge].append(i)
    info[i] = [sw, popu, edge]
info[1] = [0, 0, 0]

def dfs(now):
    count = 0
    for i in graph[now]:
        count += dfs(i)
    if info[now][0] == 'S':
        count += info[now][1]
    elif info[now][0] == 'W':
        count = max(0, count - info[now][1])
    return count

print(dfs(1))