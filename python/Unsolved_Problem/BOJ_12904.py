import sys
from collections import deque
input = sys.stdin.readline

def solution():
    start = input().rstrip()
    target = input().rstrip()
    if start == target:
        return 1
    visited = set()
    visited.add(start)
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        print(now)
        next1 = now + 'A'
        next2 = now[::-1] + 'B'
        if len(now) + 1 == len(target):
            if next1 == target or next2 == target:
                return 1
        else:
            if next1 not in visited:
                visited.add(next1)
                q.append(next1)
            if next2 not in visited:
                visited.add(next2)
                q.append(next2)
    return 0

print(solution())
