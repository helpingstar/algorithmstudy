import sys
from collections import deque

input = sys.stdin.readline


def solution():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    N = int(input())
    n_max = 0
    n_min = 101
    board = []
    for _ in range(N):
        line = list(map(int, input().split()))
        n_max = max(n_max, max(line))
        n_min = min(n_min, min(line))
        board.append(line)
    safe_max = 1

    for w in range(n_min, n_max):
        visited = [[False] * N for _ in range(N)]
        safe_count = 0
        q = deque()
        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue
                if board[r][c] > w:
                    visited[r][c] = True
                    q.append((r, c))
                    safe_count += 1
                    while q:
                        x, y = q.popleft()
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]

                            if not (0 <= nx < N and 0 <= ny < N):
                                continue
                            if visited[nx][ny]:
                                continue
                            if board[nx][ny] <= w:
                                continue

                            q.append((nx, ny))
                            visited[nx][ny] = True
        safe_max = max(safe_max, safe_count)
    print(safe_max)
    return


solution()
