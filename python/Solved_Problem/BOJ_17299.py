import sys
from collections import defaultdict, deque
input = sys.stdin.readline

count = defaultdict(int)

N = int(input())

nums = list(map(int, input().split()))

for num in nums:
    count[num] += 1

stack = deque()

ans = deque()

for num in reversed(nums):
    while stack and count[stack[-1]] <= count[num]:
        stack.pop()
    if stack:
        ans.appendleft(stack[-1])
    else:
        ans.appendleft(-1)
    stack.append(num)

print(*ans)