import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

ans = []

q = deque(list(range(1, n+1)))

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>')
