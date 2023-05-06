import sys
from collections import deque
input = sys.stdin.readline


def solution():
    parens = input().rstrip()
    answer = 0
    stack = deque()
    temp = 1
    for i, c in enumerate(parens):
        if c == '(':
            temp *= 2
            stack.append('(')
        elif c == '[':
            temp *= 3
            stack.append('[')
        elif c == ')':
            if not stack or stack[-1] == '[':
                return 0
            if parens[i-1] == '(':
                answer += temp
            stack.pop()
            temp //= 2
        else:
            if not stack or stack[-1] == '(':
                return 0
            if parens[i-1] == '[':
                answer += temp
            stack.pop()
            temp //= 3
    if stack:
        return 0
    return answer


print(solution())
