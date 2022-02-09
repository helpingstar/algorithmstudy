import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewerly = []
bag = []

for _ in range(n):
    m, v = map(int, input().split())
    jewerly.append((m, v))

for _ in range(k):
    c = int(input())
    bag.append(c)

jewerly.sort()
bag.sort()
max = -1
result = 0

q = []

j_pointer = 0

for weight in bag:
    while j_pointer < len(jewerly) and jewerly[j_pointer][0] <= weight:
        heapq.heappush(q, -jewerly[j_pointer][1])
        j_pointer += 1
    if q:
        result += -heapq.heappop(q)
    
print(result)