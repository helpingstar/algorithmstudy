from collections import deque
import sys

input = sys.stdin.readline

dx = (-1, 0, 0, 0, 0, 1)
dy = (0, -1, 1, 0, 0, 0)
dz = (0, 0, 0, -1, 1, 0)


def solution(L, R, C):
    box = []
    visited = set()
    for l in range(L):
        board = []
        for r in range(R):
            line = list(input().rstrip())
            for c, num in enumerate(line):
                if num == 'S':
                    start = (l, r, c)
                elif num == 'E':
                    target = (l, r, c)
            board.append(line)
        input()
        box.append(board)
    q = deque()
    q.append((*start, 0))
    visited.add(start)

    while q:
        x, y, z, step = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if not (0 <= nx < L and 0 <= ny < R and 0 <= nz < C):
                continue
            if (nx, ny, nz) in visited:
                continue

            if (nx, ny, nz) == target:
                return f'Escaped in {step + 1} minute(s).'

            if box[nx][ny][nz] == '#':
                continue

            q.append((nx, ny, nz, step+1))
            visited.add((nx, ny, nz))
    return 'Trapped!'


while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break

    print(solution(l, r, c))
