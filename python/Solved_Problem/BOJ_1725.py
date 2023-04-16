import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

stack = deque()

ans = 0

for i in range(N):
    if not stack:
        stack.append(i)
        continue

    while stack and nums[stack[-1]] > nums[i]:
        temp = stack.pop()
        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1

        ans = max(ans, width * nums[temp])
    stack.append(i)

while stack:
    temp = stack.pop()
    if not stack:
        width = N
    else:
        width = N - stack[-1] - 1
    ans = max(ans, width * nums[temp])

print(ans)
