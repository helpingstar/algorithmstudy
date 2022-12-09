import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = []
nums = set()
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    nums |= set(line)

def bfs(x, y, visited:set, water):
    visited.add((x, y))
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if (nx, ny) in visited:
                continue
            if board[nx][ny] > water:
                visited.add((nx, ny))
                q.append((nx, ny))
ans = 1
for water in nums:
    visited = set()
    count = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] > water and (r, c) not in visited:
                bfs(r, c, visited, water)
                count += 1
    ans = max(ans, count)

print(ans)
