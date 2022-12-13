import sys
from collections import deque

input = sys.stdin.readline

nRow, nCol = map(int, input().split())

board = []
two_ball = [-1, -1, -1, -1]

for r in range(nRow):
    line = list(input().rstrip())
    for c, element in enumerate(line):
        if element == 'o':
            if two_ball[0] == -1:
                two_ball[0] = r
                two_ball[1] = c
            else:
                two_ball[2] = r
                two_ball[3] = c
    board.append(line)

# print(two_ball)
def move_up(x, y):
    if x == 0:
        return -1, -1
    if board[x-1][y] == '#':
        return x, y
    return x-1, y

def move_down(x, y):
    if x == nRow-1:
        return -1, -1
    if board[x+1][y] == '#':
        return x, y
    return x+1, y

def move_left(x, y):
    if y == 0:
        return -1, -1
    if board[x][y-1] == '#':
        return x, y
    return x, y-1

def move_right(x, y):
    if y == nCol-1:
        return -1, -1
    if board[x][y+1] == '#':
        return x, y
    return x, y+1

def solution():
    q = deque()
    q.append((two_ball, 0))
    visited = set()
    visited.add(tuple(two_ball))
    while q:
        (x1, y1, x2, y2), count = q.popleft()
        if count == 10:
            return -1
        # print(f'[debug]  1: {x1, y1}, 2: {x2, y2}')
        for move_func in [move_up, move_down, move_left, move_right]:
            nx1, ny1 = move_func(x1, y1)
            nx2, ny2 = move_func(x2, y2)
            if (nx1, ny1, nx2, ny2) in visited:
                continue
            if (nx1 == -1 and nx2 != -1) or (nx1 != -1 and nx2 == -1):
                return count + 1
            if (nx1 != -1) and (nx2 != -1):
                q.append(((nx1, ny1, nx2, ny2), count+1))
                visited.add((nx1, ny1, nx2, ny2))
    return -1

print(solution())
