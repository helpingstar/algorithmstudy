import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

ab_dic = {}

for i in range(1, n+1):
    ab_dic[i] = []

entered_vertex = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ab_dic[a].append(b)
    ab_dic[b].append(a)
    
def bfs(x):
    if entered_vertex[x]:
        return False
    queue = deque()
    queue.append(x)
    while queue:
        t = queue.popleft()
        entered_vertex[t] = True
        for i in ab_dic[t]:
            if entered_vertex[i]:
                continue
            queue.append(i)
    return True
count = 0
for i in range(1, n+1):
    if not entered_vertex[i]:
        bfs(i)
        count += 1
        
print(count)
        