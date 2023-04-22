import sys
import heapq

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

q = []

for i in range(N):
    heapq.heappush(q, (-board[-1][i], i))

cnt = [N-1] * N

for i in range(N):
    num, idx = heapq.heappop(q)
    cnt[idx] -= 1
    heapq.heappush(q, (-board[cnt[idx]][idx], idx))

print(-num)
