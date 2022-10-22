import sys
from collections import deque

input = sys.stdin.readline

a, b, d, N = map(int, input().split())

q = deque([1] + [0] * (d-1))

baby = 0

for _ in range(N):
    baby += (q[a-1] - q[b-1])
    q.appendleft(baby % 1000)
    q.pop()

print(sum(q) % 1000)
