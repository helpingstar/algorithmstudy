import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def solution():
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    dist = [[-1] * C for _ in range(R)]
    dist[0][0] = 0

    q = deque()
    q.append((0, 0))
    answer = float('inf')
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if board[nx][ny] == 1:
                continue
            if dist[nx][ny] != -1:
                continue

            if board[nx][ny] == 2:
                temp = dist[x][y] + 1 + (R - nx) + (C - ny) - 2
                if temp <= T:
                    answer = min(answer, temp)
            else:
                if nx == R-1 and ny == C-1:
                    return min(answer, dist[x][y] + 1)

            dist[nx][ny] = dist[x][y] + 1
            if dist[nx][ny] < T:
                q.append((nx, ny))
    if answer != float('inf'):
        return answer
    else:
        return "Fail"


print(solution())
