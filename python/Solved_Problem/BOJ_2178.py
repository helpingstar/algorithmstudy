from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
moves = ((0, -1), (0, 1), (1, 0), (-1, 0))
board = []
visited = set()

for _ in range(r):
    board.append(list(map(int, list(input().rstrip()))))

def bfs():
    q = deque()
    q.append((0, 0))
    visited.add((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if board[nx][ny] == 0:
                continue
            if (nx, ny) in visited:
                continue
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))
            visited.add((nx, ny))
bfs()

print(board[r-1][c-1])
