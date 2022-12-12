import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())

assignments = []

for _ in range(n):
    a, b = map(int, input().split())
    assignments.append((a, b))

assignments.sort(key=lambda x: (-x[0], -x[1]))
q = []
cur = 0
ans = 0
for i in range(n, 0, -1):
    while cur < n and assignments[cur][0] >= i:
        heapq.heappush(q, -assignments[cur][1])
        cur += 1
    # print(f'[debug]  q: {q}')
    if q:
        ans += -heapq.heappop(q)

print(ans)
