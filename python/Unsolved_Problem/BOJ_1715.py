import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    i = int(input())
    heapq.heappush(q, i)

if n == 1:
    print(0)
else:
    ans = 0

    while len(q) > 2:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += (a+b)
        heapq.heappush(q, a+b)

    print(ans + q[0] + q[1])
