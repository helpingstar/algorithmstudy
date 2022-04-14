from os import sep
from pydoc import cli
import sys
from collections import deque

input = sys.stdin.readline

floor = int(input())
dests = [0] + list(map(int, input().split()))

graph = [[] for _ in range(floor + 1)]
indegree = [0] * (floor + 1)

client_exist = [True] * (floor + 1)

for a, b in enumerate(dests):
    graph[a].append(b)
    indegree[b] += 1

q = deque()
q.append(1)
result = []

while q:
    now = q.popleft()
    result.append(now)
    indegree[now] -= 1
    if client_exist[now]:
        q.append(dests[now])
        client_exist[now] = False
    else:
        for i in range(1, floor+1):
            if client_exist[i] and indegree[0]:
                q.append(i)
                break
print(len(result) - 1)
print(*result[1:], sep=' ')

