import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_row, n_col = map(int, input().split())

board = []

blank_list = []
virus_list = []
for r in range(n_row):
    line = list(map(int, input().split()))
    for c, num in enumerate(line):
        if num == 0:
            blank_list.append((r, c))
        elif num == 2:
            virus_list.append((r, c))
    board.append(line)

combis = combinations(blank_list, 3)
ans = 0
for comb in combis:
    t_result = len(blank_list)
    q = deque(virus_list)
    visited = set(virus_list)
    while q:
        x, y = q.popleft()
        # print(f'[debug] {x, y}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_row and 0 <= ny < n_col):
                continue
            if (nx, ny) in comb or board[nx][ny] == 1:
                continue
            if (nx, ny) in visited:
                continue
            t_result -= 1
            q.append((nx, ny))
            visited.add((nx, ny))
    ans = max(ans, t_result)

print(ans-3)
