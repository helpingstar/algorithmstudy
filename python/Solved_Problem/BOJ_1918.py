import sys
from collections import deque

input = sys.stdin.readline

equation = input().rstrip()

answer = ""
stk = deque()

op = {'/', '*', '+', '-'}
prior = {'/' : 2, '*' : 2, '-' : 1, '+' : 1, '(' : 0}

for char in equation:
    if char == '(':
        stk.append(char)
    elif char == ')':
        while stk[-1] != '(':
            answer += stk.pop()
        stk.pop()
    elif char in op:
        if stk:
            while stk and prior[stk[-1]] >= prior[char]:
                answer += stk.pop()
        stk.append(char)
    else:
        answer += char

while stk:
    answer += stk.pop()

print(answer)
