import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

parents = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
to_leaf = [0] * (n+1)

for c, p in enumerate(parents[1:], 1):
    graph[p].append(c)

def init(now):
    if not graph[now]:
        return 0
    road_leaf = 0
    for next in graph[now]:
        road_leaf = max(road_leaf, init(next))
    to_leaf[now] = road_leaf + 1
    return to_leaf[now]

init(0)

# print(graph)
# print(to_leaf)

q = deque()
q.append((0, 0))

ans = 0

while q:
    now, time = q.popleft()
    ans = max(ans, time)
    for idx, next in enumerate(sorted(graph[now], key=lambda x: (-max(to_leaf[x], len(graph[x])), (-to_leaf[x]-len(graph[x])))), 1):
        q.append((next, time+idx))
print(ans)
