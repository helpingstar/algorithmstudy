import sys
import heapq
input = sys.stdin.readline

N = int(input())
temp = []
for _ in range(N):
    a, b = map(int, input().split())
    if b < a:
        temp.append((b, a))
    else:
        temp.append((a, b))

roads = []

train = int(input())

for start, end in temp:
    if end - start > train:
        continue
    roads.append((start, end))

roads.sort(key=lambda x: (x[1], x[0]))
q = []
ans = 0
for start, end in roads:
    heapq.heappush(q, start)
    
    while q and q[0] < (end-train):
        heapq.heappop(q)
    
    ans = max(ans, len(q))
         
print(ans)