import sys
from collections import deque
input = sys.stdin.readline

def check(string):
    stack = deque()
    for c in string:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

    if stack:
        return False
    else:
        return True

ans = 0
for _ in range(int(input())):
    word = input().rstrip()
    ans += check(word)

print(ans)
