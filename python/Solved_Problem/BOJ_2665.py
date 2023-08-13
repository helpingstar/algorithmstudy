import sys
import heapq

input = sys.stdin.readline

def solution():
    INF = 10000
    N = int(input())
    dist = [[INF] * N for _ in range(N)]
    board = [list(input().rstrip()) for _ in range(N)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    dist[0][0] = 0
    q = []
    q.append((0, 0, 0))

    while q:
        _, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if dist[nx][ny] <= dist[x][y]:
                continue

            if board[nx][ny] == "1":
                dist[nx][ny] = dist[x][y]
            else:
                dist[nx][ny] = dist[x][y] + 1
            q.append((dist[nx][ny], nx, ny))
    print(dist[N - 1][N - 1])

solution()
