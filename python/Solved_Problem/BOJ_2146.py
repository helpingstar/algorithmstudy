import sys
from collections import defaultdict, deque
input = sys.stdin.readline

island_pos = defaultdict(list)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def collect_pos(x, y, region_name):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    island_pos[region_name].append((x, y))
    board[x][y] = region_name
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            island_pos[region_name].append((nx, ny))
            visited[nx][ny] = True
            q.append((nx, ny))
            board[nx][ny] = region_name

count = 1
for r in range(n):
    for c in range(n):
        if board[r][c] == 1 and not visited[r][c]:
            collect_pos(r, c, count)
            count += 1

# print(board)

def find_bridge(region_name):
    bridge = [[-1] * n for _ in range(n)]

    for x, y in island_pos[region_name]:
        bridge[x][y] = 0

    q = deque(island_pos[region_name])
    while q:
        x, y = q.popleft()
        # print(f'[debug] (x, y): {(x, y)}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if bridge[nx][ny] != -1:
                continue
            if board[nx][ny] > 0 and board[nx][ny] != region_name:
                return bridge[x][y]
            q.append((nx, ny))
            bridge[nx][ny] = bridge[x][y] + 1

ans = 100000
for i in range(1, count):
    # print(f'[debug] i: {i}')
    ans = min(ans, find_bridge(i))

print(ans)
