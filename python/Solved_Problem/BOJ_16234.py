import sys
from collections import deque


def solution():
    input = sys.stdin.readline

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    size, low, high = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size)]

    visited = [[-1] * size for _ in range(size)]

    def bfs(x, y, cnt):
        q = deque()
        q.append((x, y))
        visited[x][y] = cnt
        track = [(x, y)]
        total = board[x][y]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < size and 0 <= ny < size):
                    continue
                if visited[nx][ny] == cnt:
                    continue
                if not (low <= abs(board[x][y] - board[nx][ny]) <= high):
                    continue

                q.append((nx, ny))
                visited[nx][ny] = cnt
                track.append((nx, ny))
                total += board[nx][ny]

        if len(track) == 1:
            return False
        population = total // len(track)
        for x, y in track:
            board[x][y] = population
        return True

    count = 0
    while True:
        flag = False
        for r in range(size):
            for c in range(size):
                if visited[r][c] != count:
                    flag |= bfs(r, c, count)
        if not flag:
            print(count)
            return
        count += 1


solution()
