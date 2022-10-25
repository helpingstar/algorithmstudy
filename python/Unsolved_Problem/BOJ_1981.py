import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    ans = 300
    q = deque()
    q.append((board[x][y], board[x][y], x, y, []))
    while q:
        n_min, n_max, x, y, trace = q.popleft()
        if x == n-1 and y == n-1:
            ans = min(ans, n_max - n_min)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in trace:
                continue
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            temp_min = min(n_min, board[nx][ny])
            temp_max = max(n_max, board[nx][ny])
            if (temp_max - temp_min) > ans:
                continue

            q.append((temp_min, temp_max, nx, ny, trace + [(nx, ny)]))
    return ans

print(bfs(0, 0))
