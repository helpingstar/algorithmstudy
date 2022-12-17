import sys
from collections import deque
input = sys.stdin.readline

target = int(input())

n_edge = int(input())

graph = [[] for _ in range(target+1)]

indegree = [0] * (target + 1)
need = [0] * (target + 1)
need[target] = 1
is_basic = [True] * (target + 1)

for _ in range(n_edge):
    a, b, c = map(int, input().split())
    is_basic[a] = False
    graph[a].append((b, c))
    indegree[b] += 1


q = deque()
for i, num in enumerate(indegree):
    if num == 0:
        q.append(i)
while q:
    now = q.popleft()
    for next, num in graph[now]:
        indegree[next] -= 1
        need[next] += (need[now] * num)
        if indegree[next] == 0:
            q.append(next)

for i in range(1, target+1):
    if is_basic[i]:
        print(i, need[i])
    