import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    left = deque()
    right = deque()

    for c in word:
        if c == '<':
            if left:
                right.appendleft(left.pop())
        elif c == '>':
            if right:
                left.append(right.popleft())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    print(*left, *right, sep='')
