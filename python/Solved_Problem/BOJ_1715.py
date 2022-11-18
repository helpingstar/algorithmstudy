import sys
import heapq

input = sys.stdin.readline

q = []
n_card = int(input())

for _ in range(n_card):
    card = int(input())
    heapq.heappush(q, card)

ans = 0

while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    temp = a + b
    q.append(temp)
    ans += temp

print(ans)
