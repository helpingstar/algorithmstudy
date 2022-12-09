import sys
from collections import deque
input = sys.stdin.readline

dx = (1, 1, 1, 0, 0, -1, -1, -1)
dy = (0, 1, -1, 1, -1, 0, 1, -1)

def bfs(x, y, visited, board, width, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < height and 0 <= ny < width):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    # print(visited)



while True:
    width, height = map(int, input().split())
    if width + height == 0:
        break
    visited = []
    board = []
    for _ in range(height):
        row = list(map(int, input().split()))
        board.append(row)
        visited.append([False] * width)
    # bfs
    count = 0
    for r in range(height):
        for c in range(width):
            if board[r][c] == 1 and not visited[r][c]:
                bfs(r, c, visited, board, width, height)
                count += 1
    print(count)
