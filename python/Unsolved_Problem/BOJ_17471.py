import sys
import itertools
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize

def bfs(pos_list):
    start = pos_list[0]
    q = deque()
    visited = set()

    q.append(start)
    visited.add(start)
    total = 0
    while q:
        now = q.popleft()
        total += populations[now]
        for next in graph[now]:
            if next not in visited and next in pos_list:
                q.append(next)
                visited.add(next)
    return total, len(visited)

n = int(input())
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
result = INF



for i in range(1, n+1):
    temp = list(map(int, input().split()))
    graph[i] += temp[1:]

for i in range(1, n//2 + 1):
    combis = list(itertools.combinations(range(1, n+1), i))

    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(1, n+1) if i not in combi])
        if v1 + v2 == n:
            if abs(sum1 - sum2) < result:
                result = abs(sum1 - sum2)

if result != INF:
    print(result)
else:
    print(-1)
