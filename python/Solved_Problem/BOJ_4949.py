import sys
from collections import deque

input = sys.stdin.readline
ans = []
while True:
    stack = deque()
    success_flag = True
    line = input().rstrip()
    if line == '.':
        break
    for c in line:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack:
                success_flag = False
                ans.append('no')
                break
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                success_flag = False
                ans.append('no')
                break
        elif c == ']':
            if not stack:
                success_flag = False
                ans.append('no')
                break
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                success_flag = False
                ans.append('no')
                break
    if success_flag:
        if stack:
            ans.append('no')
        else:
            ans.append('yes')
print(*ans, sep='\n')
