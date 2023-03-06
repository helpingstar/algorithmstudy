import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, visited):
    cnt = 1
    positions = [(x, y)]
    populations = board[x][y]
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(board[nx][ny] - board[x][y]) <= R:
                positions.append((nx, ny))
                populations += board[nx][ny]
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    temp = populations // cnt
    for x, y in positions:
        board[x][y] = temp
    return cnt

def solution():
    count = 0
    for _ in range(2000):
        flag = False
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    cnt = bfs(r, c, visited)
                    if cnt > 1:
                        flag = True

        if not flag:
            return count
        count += 1

        # print('-'*9)
        # print(*board, sep='\n')
        # print('-'*9)

print(solution())
