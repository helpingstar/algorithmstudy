import sys
from collections import deque

input = sys.stdin.readline

def solution():
    SIZE, STEP = map(int, input().split())
    # 0: left, 1: right
    bridge = (tuple(input().rstrip()), tuple(input().rstrip()))
    visited = [[False] * SIZE for _ in range(2)]
    # print(bridge)
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        lr, idx, cnt = q.popleft()

        if idx + 1 >= SIZE:
            return 1
        if idx + STEP >= SIZE:
            return 1
        if bridge[lr][idx+1] == '1' and not visited[lr][idx+1]:
            q.append((lr, idx+1, cnt+1))
            visited[lr][idx+1] = True
        if bridge[lr][idx-1] == '1' and not visited[lr][idx-1] and idx-1 >= cnt+1:
            q.append((lr, idx-1, cnt+1))
            visited[lr][idx-1] = True
        if bridge[lr ^ 1][idx+STEP] == '1' and not visited[lr ^ 1][idx+STEP]:
            q.append((lr ^ 1, idx+STEP, cnt+1))
            visited[lr ^ 1][idx+STEP] = True
    return 0


print(solution())