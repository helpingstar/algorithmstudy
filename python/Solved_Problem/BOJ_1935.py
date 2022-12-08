import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
line = input().rstrip()

alphabet_nubmer_map = []
for _ in range(n):
    alphabet_nubmer_map.append(int(input()))

def s2n(num):
    if isinstance(num, int) or isinstance(num, float):
        return num
    if num.isdigit():
        return float(num)
    else:
        return alphabet_nubmer_map[ord(num) - ord('A')]

def cal(a, b, c):
    if c == '+':
        return s2n(a) + s2n(b)
    elif c == '-':
        return s2n(a) - s2n(b)
    elif c == '*':
        return s2n(a) * s2n(b)
    else:
        return s2n(a) / s2n(b)

stack = deque()
for c in line:
    if c in '+-/*':
        b = stack.pop()
        a = stack.pop()
        stack.append(cal(a, b, c))
    else:
        stack.append(c)
print(f'{stack[0]:.2f}')
