import sys
from collections import deque
input = sys.stdin.readline

def solution():
    SIZE = 10
    board = [list(map(int, input().split())) for _ in range(SIZE)]
    visited = [[False] * SIZE for _ in range(SIZE)]
    island_list = []
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        i_set = set()
        i_set.add((x, y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                    continue
                if board[nx][ny] == 0:
                    continue
                if visited[nx][ny]:
                    continue
                q.append((nx, ny))
                i_set.add((nx, ny))
                visited[nx][ny] = True
        island_list.append(i_set)

    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 1 and not visited[r][c]:
                bfs(r, c)

    s_island_list = []
    for i in range(len(island_list)):
        s_island_list.append(sorted(list(island_list[i])))

    def dp(cur, cnt, start):


solution()
