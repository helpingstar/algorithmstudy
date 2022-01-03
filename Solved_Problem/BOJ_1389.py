import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
guys = {}
for i in range(1, n+1):
    guys[i] = set()



for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    guys[a].add(b)
    guys[b].add(a)

def bfs(x):
    guy_count = [101] * (n + 1)
    guy_count[0] = 0
    queue = deque()
    queue.append(x)
    guy_count[x] = 0
    while queue:
        p = queue.popleft()
        for guy in guys[p]:
            if guy_count[guy] > guy_count[p] + 1:
                guy_count[guy] = guy_count[p] + 1
                queue.append(guy)
    return guy_count
        
min_list = []

for i in range(1, n+1):
    min_list.append(sum(bfs(i)))
    
print(min_list.index(min(min_list)) + 1)