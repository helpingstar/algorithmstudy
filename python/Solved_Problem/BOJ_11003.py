import sys
from collections import deque
input = sys.stdin.readline

ans = []

N, L = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()

for i, num in enumerate(nums):
    while q and q[-1][0] > num:
        q.pop()

    while q and q[0][1] <= i - L:
        q.popleft()

    q.append((num, i))

    ans.append(q[0][0])

print(*ans)
