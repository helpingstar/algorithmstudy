import sys
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

input = sys.stdin.readline

n_size = int(input())

board = []

def next_fish(size, pos):
    x, y = pos
    q = deque()
    q.append((x, y, 0))
    visited = set()
    visited.add((x, y))
    candidate = []
    step = 1000
    while q:
        x, y, cnt = q.popleft()
        # print(f'[debug] next_fish  {x, y, cnt}')
        if cnt >= step:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_size and 0 <= ny < n_size):
                continue
            if board[nx][ny] > size:
                continue
            if (nx, ny) in visited:
                continue
            if board[nx][ny] == 0 or board[nx][ny] == size:
                q.append((nx, ny, cnt+1))
                visited.add((nx, ny))
            else:
                candidate.append((nx, ny))
                step = cnt+1
    if not candidate:
        return -1, -1, -1

    candidate.sort()
    return candidate[0][0], candidate[0][1], step


for r in range(n_size):
    line = list(map(int, input().split()))
    for c, num in enumerate(line):
        if num == 9:
            baby_pos = [r, c]
            line[c] = 0
    board.append(line)

result = 0
level = [2, 0]
r, c = baby_pos
while True:
    nr, nc, step = next_fish(level[0], (r, c))
    # print(f'[debug]  {nr, nc, step}')
    if nr == -1:
        break
    result += step
    level[1] += 1
    if level[0] == level[1]:
        level[0] += 1
        level[1] = 0
    board[nr][nc] = 0
    r, c = nr, nc
print(result)
