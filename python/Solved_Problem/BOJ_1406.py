import sys
from collections import deque
input = sys.stdin.readline

first = input().rstrip()
stack = deque()
for c in first:
    stack.append(c)

right_stack = deque()

n = int(input())

for _ in range(n):
    com = input().rstrip()

    if com == 'L':
        if stack:
            right_stack.append(stack.pop())
    elif com == 'B':
        if stack:
            stack.pop()
    elif com == 'D':
        if right_stack:
            stack.append(right_stack.pop())
    else:
        stack.append(com[2])

left = ''.join(stack)
right = ''.join(right_stack)

print(left + right[::-1])
