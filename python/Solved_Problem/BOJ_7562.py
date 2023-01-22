import sys
from collections import deque

dx = (-2, -2, -1, -1, 1, 1, 2, 2)
dy = (-1, 1, -2, 2, -2, 2, -1, 1)

input = sys.stdin.readline

T = int(input())

def solution():
    n_size = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        return 0
    visited = set()
    visited.add(start)
    q = deque()
    q.append((*start, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) == end:
                return cnt + 1
            if not (0 <= nx < n_size and 0 <= ny < n_size):
                continue
            if (nx, ny) in visited:
                continue
            q.append((nx, ny, cnt+1))
            visited.add((nx, ny))

for _ in range(T):
    print(solution())
