import sys
from collections import deque
input = sys.stdin.readline

# apple : 5
# snake : 1
# blank : 0

"""
0 : left
1 : down
2 : right
3 : up
"""

n_board = int(input())
n_apple = int(input())

board = [[0] * n_board for _ in range(n_board)]
board[0][0] = 1
snake = deque()
snake.append((0, 0))

# def next_delta(now, curve):
#     if now == 0:
#         if curve == 'L': # 
#             return (1, 0, 1)
#         else:
#             return (-1, 0, 3)
#     elif now == 1:
#         if curve == 'L':
#             return (0, 1, 2)
#         else:
#             return (0, -1, 0)
#     elif now == 2:
#         if curve == 'L':
#             return (-1, 0, 3)
#         else:
#             return (1, 0, 1)
#     else:
#         if curve == 'L':
#             return (0, -1, 0)
#         else:
#             return (0, 1, 2)

def next_delta(now, curve):
    if now == 0:
        if curve == 'L': # 
            return 1
        else:
            return 3
    elif now == 1:
        if curve == 'L':
            return 2
        else:
            return 0
    elif now == 2:
        if curve == 'L':
            return 3
        else:
            return 1
    else:
        if curve == 'L':
            return 0
        else:
            return 2

def dir_delta(way):
    if way == 0:
        return (0, -1)
    elif way == 1:
        return (1, 0)
    elif way == 2:
        return (0, 1)
    else:
        return (-1, 0)

for _ in range(n_apple):
    a, b = map(int, input().split())
    board[a-1][b-1] = 5

n_map = int(input())
maps = dict()
for _ in range(n_map):
    a, b = input().split()
    maps[int(a)] = b

x, y = 0, 0
way = 2
cnt = 0
while True:
    cnt += 1
    
    # if cnt in maps:
    #     dx, dy, way = next_delta(way, maps[cnt])
    # else:
    #     dx, dy = dir_delta(way)
    
    dx, dy = dir_delta(way)
    nx = x + dx
    ny = y + dy
    
    if cnt in maps:
        way = next_delta(way, maps[cnt])
    
    if not (0 <= nx < n_board and 0 <= ny < n_board):
        # print(*board, sep='\n')
        # print(f'out {x, y} -> {nx, ny}')
        break
    if board[nx][ny] == 1:
        # print(*board, sep='\n')
        # print(f'snake {x, y} -> {nx, ny}')
        break
    
    if board[nx][ny] == 0:
        sx, sy = snake.popleft()
        board[sx][sy] = 0
    board[nx][ny] = 1
    snake.append((nx, ny))
    
    x, y = nx, ny
    
print(cnt)