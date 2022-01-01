import sys
import heapq

n = int(sys.stdin.readline().rstrip())

ns = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if ns:
            a, b = heapq.heappop(ns)
            print(a * b)
        else:
            print(0)
    elif x < 0:
        heapq.heappush(ns, (abs(x), -1))
    else:
        heapq.heappush(ns, (x, 1))
    