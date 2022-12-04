import sys
import heapq

input = sys.stdin.readline

n = int(input())

left = []
right = []
mid = int(input())
print(mid)
for _ in range(n-1):
    a = int(input())
    if a < mid:
        heapq.heappush(left, -a)  # max-heap
    else:
        heapq.heappush(right, a)  # min-heap
    if len(left) > len(right):
        heapq.heappush(right, mid)
        mid = -heapq.heappop(left)
    elif len(left) + 1 < len(right):
        heapq.heappush(left, -mid)
        mid = heapq.heappop(right)
    print(mid)
