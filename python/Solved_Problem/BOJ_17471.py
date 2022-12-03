import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n_city = int(input())

populations = [0] + list(map(int, input().split()))

graph = [[]]

for i in range(1, n_city+1):
    temp = list(map(int, input().split()))
    graph.append(temp[1:])

def bfs(arr):
    # print(f'[debug]  {arr}')
    start = arr[0]
    score = populations[start]
    visited = set()
    visited.add(start)
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if next in visited:
                continue
            if next not in arr:
                continue
            q.append(next)
            visited.add(next)
            score += populations[next]
    return score, len(visited)

ans = 100000
for i in range(1, n_city // 2 + 1):
    for comb in combinations(range(1, n_city+1), i):
        # print(f'debug [comb] : {comb}')
        s1, v1 = bfs(comb)
        s2, v2 = bfs([i for i in range(1, n_city+1) if i not in comb])
        if v1+v2 == n_city:
            # print(f'debug s1:{s1}, v1:{v1}')
            # print(f'debug s2:{s2}, v2:{v2}')
            ans = min(ans, abs(s1-s2))

if ans == 100000:
    print(-1)
else:
    print(ans)
