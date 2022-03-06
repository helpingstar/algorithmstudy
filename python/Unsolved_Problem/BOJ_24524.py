import sys
from collections import deque

input = sys.stdin.readline

s = list(input().rstrip())
t = input().rstrip()
t_set = set(t)
t_len = len(t)
stack = []

result = 0

for c in s:
    if c in t:
        stack.append(c)
        if len(stack) >= len(t):
            if stack[-t_len:] == list(t):
                for _ in range(t_len):
                    stack.pop()
                result += 1

print(result)