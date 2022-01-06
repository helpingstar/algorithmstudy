import sys
from collections import deque
from collections import defaultdict
n, m = map(int, sys.stdin.readline().split())

node = defaultdict(set)
entered_vertex = {}
all_n = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a].add(b)
    node[b].add(a)
    all_n.add(a)
    all_n.add(b)

for i in all_n:
    entered_vertex[i] = False

def bfs(x):
    if entered_vertex[x]:
        return False
    queue = deque()
    queue.append(x)
    while queue:
        t = queue.popleft()
        entered_vertex[t] = True
        for i in node[t]:
            if entered_vertex[i]:
                continue
            queue.append(i)
    return True

count = 0
for i in all_n:
    if bfs(i):
        count += 1
        
print(count)
        