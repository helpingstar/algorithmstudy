from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())

node = {}


for i in range(1, n+1):
    node[i] = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].add(b)
    node[b].add(a)
    
dfs_enter_vertex = [False] * (n+1)
dfs_enter_vertex[v] = True

def dfs(x):
    for no in node[x]:
        if not dfs_enter_vertex[no]:
            print(no, end=' ')
            dfs_enter_vertex[no] = True
            dfs(no)

bfs_enter_vertex = [False] * (n+1)

def bfs(x):
    enter_order = []
    queue = deque()
    queue.append(x)
    bfs_enter_vertex[x] = True
    while queue:
        t = queue.popleft()
        enter_order.append(t)
        for no in node[t]:
            if not bfs_enter_vertex[no]:
                bfs_enter_vertex[no] = True
                queue.append(no)
    return enter_order

print(v, end=' ')
dfs(v)
print()
for i in bfs(v):
    print(i, end=' ')