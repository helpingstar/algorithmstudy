"""북쪽을 보고있으면 서쪽을 가야하는데
북쪽을 보고있으면 북쪽 먼저 가는 것으로 착각함"""

import sys

input = sys.stdin.readline

h, w = map(int ,input().split())
x, y, dir = map(int, input().split())

board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

visited = [[False] * w for _ in range(h)]

def next_pos(x, y, dir):
    if dir == 0:
        return x, y-1
    elif dir == 1:
        return x-1, y
    elif dir == 2:
        return x, y+1
    else:
        return x+1, y


turn_left = [0, 3, 2, 1]

def next_dir(dir):
    if dir == 0:
        return 3
    elif dir == 3:
        return 2
    elif dir == 2:
        return 1
    else:
        return 0

def get_behind(x, y, dir):
    if dir == 0:
        return x+1, y
    elif dir == 1:
        return x, y-1
    elif dir == 2:
        return x-1, y
    else:
        return x, y+1

count = 1
visited[x][y] = True

while True:
    turn_four = True
    for _ in range(4):
        nx, ny = next_pos(x, y, dir)
        if board[nx][ny] != 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            count += 1
            x, y = nx, ny
            turn_four = False
            dir = next_dir(dir)
            break
        dir = next_dir(dir)
    if turn_four:
        bx, by = get_behind(x, y, dir)
        if board[bx][by] == 1:
            break
        else:
            x, y = bx, by

print(count)       
    
