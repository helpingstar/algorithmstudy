import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stack = deque()
ans = deque()
for i in reversed(nums):
    while stack and stack[-1] <= i:
        stack.pop()
    if not stack:
        ans.appendleft(-1)
    else:
        ans.appendleft(stack[-1])
    # print(stack)
    stack.append(i)

print(*ans)