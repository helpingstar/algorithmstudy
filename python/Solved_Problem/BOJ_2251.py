import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())

bottles = [0, 0, c]

q = deque()
q.append((0, 0, c))
visited = set()
visited.add((0, 0, c))
answer = []
while q:
    x, y, z = q.popleft()

    if x == 0:
        answer.append(z)

    candidate = []

    xy = min(x, b - y)
    xz = min(x, c - z)

    candidate.append((x - xy, y + xy, z))
    candidate.append((x - xz, y,      z + xz))

    yx = min(y, a - x)
    yz = min(y, c - z)

    candidate.append((x + yx, y - yx, z))
    candidate.append((x,      y - yz, z + yz))

    zx = min(z, a - x)
    zy = min(z, b - y)

    candidate.append((x + zx, y,      z - zx))
    candidate.append((x,      y + zy, z - zy))

    for nx, ny, nz in candidate:
        if (nx, ny, nz) not in visited:
            visited.add((nx, ny, nz))
            q.append((nx, ny, nz))

print(*sorted(answer))
