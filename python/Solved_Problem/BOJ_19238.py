import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_size, n_client, fuel = map(int, input().split())

board = []
for _ in range(n_size):
    board.append(list(map(int, input().split())))

sx, sy = map(int, input().split())

client_list = []

for _ in range(n_client):
    a, b, c, d = map(int, input().split())
    client_list.append([a, b, c, d])

def bfs(sx, sy):
    distance = [[-1] * n_size for _ in range(n_size)]
    distance[sx][sy] = 0
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_size and 0 <= ny < n_size):
                continue
            if board[nx][ny] == 1:
                continue
            if distance[nx][ny] != -1:
                continue
            q.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1
    return distance

def solution():
    global fuel
    global sx, sy
    for _ in range(n_client):
        visited = bfs(sx-1, sy-1)

        for i in range(len(client_list)):
            c_s_x, c_s_y, _, _ = client_list[i]
            client_list[i].append(visited[c_s_x-1][c_s_y-1])

        client_list.sort(key=lambda x: (-x[-1], -x[0], -x[1]))

        # print(f'[debug]  start: {client_list}')

        start_x, start_y, end_x, end_y, dist = client_list.pop()
        for i in range(len(client_list)):
            client_list[i].pop()

        visited = bfs(start_x-1, start_y-1)
        dist2 = visited[end_x-1][end_y-1]

        # print(f'[debug]  end: {dist2}')
        if dist==-1 or dist2 == -1:
            return -1

        if dist + dist2 > fuel:
            return -1

        fuel -= (dist + dist2)

        fuel += dist2*2

        sx, sy = end_x, end_y
    return fuel

print(solution())
