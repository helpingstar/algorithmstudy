import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

com = {}

for i in range(1, n+1):
    com[i] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    com[a].append(b)
    com[b].append(a)

entered = [False] * (n + 1)
# entered[1] = True
def bfs():
    count = 0
    queue = deque()
    queue.append(1)
    while queue:
        t = queue.popleft()
        for i in com[t]:
            if entered[i]:
                continue
            queue.append(i)
            entered[i] = True
            count += 1
    return count

print(bfs() - 1)