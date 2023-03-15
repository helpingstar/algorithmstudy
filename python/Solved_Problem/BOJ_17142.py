import sys
from itertools import combinations
from collections import deque

INF = int(1e7)

input = sys.stdin.readline

N, n_virus = map(int, input().split())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

virus_pos = []
n_blank = 0

board = []
for r in range(N):
    line = list(map(int, input().split()))
    for c, num in enumerate(line):
        if num == 0:
            n_blank += 1
        elif num == 2:
            virus_pos.append((r, c))
    board.append(line)


def solution(comb):
    if n_blank == 0:
        return 0
    visited = set()
    left_blank = n_blank
    # max_step = float('inf')
    q = deque()
    for r, c in comb:
        q.append((r, c, 0))
        visited.add((r, c))
    while q:
        x, y, step = q.popleft()
        # max_step =
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if board[nx][ny] == 1:
                continue
            if (nx, ny) in visited:
                continue

            if board[nx][ny] == 0:
                left_blank -= 1
                if left_blank == 0:
                    return step + 1
            q.append((nx, ny, step+1))
            visited.add((nx, ny))
    return INF


ans = INF
for comb in combinations(virus_pos, n_virus):
    ans = min(ans, solution(comb))

if ans == INF:
    print(-1)
else:
    print(ans)
