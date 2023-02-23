import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
stack = deque()
ans = deque()
for i, num in enumerate(nums, 1):
    # print(f'[debug] {i, num}')
    while stack and stack[-1][0] <= num:
        stack.pop()
    
    if not stack:
        ans.append(0)
    else:
        ans.append(stack[-1][1])
    
    stack.append((num, i))

print(*ans)