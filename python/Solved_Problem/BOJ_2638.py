import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    entered = []
    for _ in range(n):
        entered.append([False] * m)
    
    cheese_touch = defaultdict(int)
    all_zero = True
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if entered[nx][ny]:
                continue
            if matrix[nx][ny] == 1:
                cheese_touch[(nx, ny)] += 1
                all_zero = False
            else:
                entered[nx][ny] = True
                queue.append((nx, ny))
    for key in cheese_touch:
        cx, cy = key
        if cheese_touch[(cx,cy)] >= 2:
            matrix[cx][cy] = 0
    return all_zero

total = 0
for line in matrix:
    total += sum(line)
if total == 0:
    print(0)
else:
    count = 0
    while not bfs():
        count += 1

    print(count)