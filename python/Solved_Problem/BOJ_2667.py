import sys
from collections import deque


def solution():
    input = sys.stdin.readline

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        cnt = 1
        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if visited[nx][ny]:
                    continue
                if board[nx][ny] == '0':
                    continue

                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
        return cnt
    ans = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == '1' and not visited[r][c]:
                ans.append(bfs(r, c))

    print(len(ans))
    print(*sorted(ans), sep='\n')


solution()
