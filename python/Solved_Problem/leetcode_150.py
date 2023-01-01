from collections import deque

def calculate(ex, a, b):
    b = int(b)
    a = int(a)
    if ex == '+':
        return a + b
    elif ex == '-':
        return a - b
    elif ex == '*':
        return a * b
    else:
        temp = abs(a) // abs(b)
        if a * b < 0:
            temp *= -1
        return temp
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        q = deque()
        cal = {'+', '-', '*', '/'}
        for v in tokens:
            if v in cal:
                b = q.pop()
                a = q.pop()
                q.append(calculate(v, a, b))
            else:
                q.append(v)
            # print(q)
        return q[0]
