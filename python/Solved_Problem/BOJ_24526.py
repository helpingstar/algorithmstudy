import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n_member, n_edge = map(int, input().split())
graph = defaultdict(list)

indegree = [0] * (n_member+1)
for _ in range(n_edge):
    a, b = map(int, input().split())

    graph[b].append(a)
    indegree[a] += 1

q = deque()
ans = 0
for i in range(1, n_member+1):
    if indegree[i] == 0:
        q.append(i)
        ans += 1

while q:
    now = q.popleft()
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
            ans += 1

print(ans)
