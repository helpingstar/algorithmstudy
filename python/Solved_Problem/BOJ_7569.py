import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)


y, x, z = map(int, input().split())

box = []
old_tomato_list = []
for z_pos in range(z):
    board = []
    for x_pos in range(x):
        temp = list(map(int, input().split()))
        for y_pos, tomato in enumerate(temp):
            if tomato == 1:
                old_tomato_list.append([z_pos, x_pos, y_pos])
        board.append(temp)
    box.append(board)

# print(box)

def check_box():
    have_zero = False
    max_num = 0
    for z_pos in range(z):
        for x_pos in range(x):
            for y_pos in range(y):
                if box[z_pos][x_pos][y_pos] == 0:
                    have_zero = True
                max_num = max(max_num, box[z_pos][x_pos][y_pos])
    return have_zero, max_num


def solution():
    bfs()
    have_zero, max_num = check_box()
    if have_zero:
        return -1
    return max_num-1


def bfs():
    q = deque(old_tomato_list)
    while q:
        pz, px, py = q.popleft()
        for i in range(6):
            nx = px + dx[i]
            ny = py + dy[i]
            nz = pz + dz[i]

            if not (0 <= nx < x and 0 <= ny < y and 0 <= nz < z):
                continue
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[pz][px][py] + 1
                q.append((nz, nx, ny))

print(solution())
