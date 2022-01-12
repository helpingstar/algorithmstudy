import sys
import heapq

n = int(sys.stdin.readline().rstrip())

ns = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if ns:
            print(-1 * heapq.heappop(ns))
        else:
            print(0)
    else:
        heapq.heappush(ns, -x)