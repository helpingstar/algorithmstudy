import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int ,input().split())

degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = deque()
answer = []

for _ in range(m):
    temp = list(map(int, input().split()))

    for i in range(1, temp[0]):
        graph[temp[i]].append(temp[i+1])
        degree[temp[i+1]] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)

    for next in graph[now]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

if sum(degree) == 0:
    print(*answer, sep='\n')
else:
    print(0)
