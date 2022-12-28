import sys
from collections import deque

input = sys.stdin.readline

n, erase = map(int, input().split())

number = input().rstrip()

stack = deque()

cur = 0

for i, num in enumerate(number):
    while stack and stack[-1] < num and erase > 0:
        stack.pop()
        erase -= 1
    stack.append(num)
    if erase == 0:
        break

if erase:
    print(''.join(stack)[:-erase])
else:
    print(''.join(stack) + number[i+1:])
