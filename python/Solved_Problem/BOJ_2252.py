import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n_student, n_compare = map(int , input().split())

degree = defaultdict(int)
graph = defaultdict(list)
visited = set()
for _ in range(n_compare):
    a, b = map(int, input().split())
    degree[b] += 1
    graph[a].append(b)

q = deque()
ans = []
for i in range(1, n_student+1):
    if degree[i] == 0:
        q.append(i)
        visited.add(i)
        ans.append(i)
while q:
    now = q.popleft()
    for next in graph[now]:
        if next in visited:
            continue
        degree[next] -= 1
        if degree[next] == 0:
            ans.append(next)
            visited.add(next)
            q.append(next)

print(*ans)
