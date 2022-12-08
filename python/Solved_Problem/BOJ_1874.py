import sys
from collections import deque
input = sys.stdin.readline

def solution():
    ans = []
    n = int(input())
    i = 1
    stack = deque()
    for _ in range(n):
        a = int(input())
        if not stack:
            if i > n:
                return 'NO'
            stack.append(i)
            i += 1
            ans.append('+')
        if a < stack[-1]:
            while a != stack[-1]:
                if not stack:
                    return 'NO'
                stack.pop()
                ans.append('-')
        elif a > stack[-1]:
            while i != a:
                stack.append(i)
                i += 1
                ans.append('+')
                if i > n:
                    return 'NO'
            stack.append(i)
            i += 1
            ans.append('+')
        stack.pop()
        ans.append('-')
        # print(f'[debug]  stack : {stack}')
        # print(f'[debug]  ans   : {ans}')
    return ans

result = solution()

if result == 'NO':
    print('NO')
else:
    print(*result, sep='\n')
