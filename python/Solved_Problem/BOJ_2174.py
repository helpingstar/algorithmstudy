import sys
from collections import defaultdict

NEXT = {
    'N' : (1, 0),
    'E' : (0, 1),
    'W' : (0, -1),
    'S' : (-1, 0)
}

ROTATE_R = 'NESW'
ROTATE_L = 'NWSE'

input = sys.stdin.readline

width, height = map(int, input().split())

board = [[0 for _ in range(width+1)] for _ in range(height+1)]

n_robot, n_oper = map(int, input().split())

robot_dir = ['']
robot_pos = [[]]

for i in range(1, n_robot+1):
    c, r, dir = input().split()
    c, r = int(c), int(r)
    board[r][c] = i
    robot_dir.append(dir)
    robot_pos.append([r, c])

def solution():
    operations = []
    for _ in range(n_oper):
        robot, oper, iter = input().split()
        operations.append([int(robot), oper, int(iter)])
    for robot, oper, iter in operations:
        if oper == 'F':
            for _ in range(iter):
                r, c = robot_pos[robot]
                dx, dy = NEXT[robot_dir[robot]]
                nr, nc = r + dx, c + dy

                if not (0 < nc <= width and 0 < nr <= height):
                    return f'Robot {robot} crashes into the wall'

                if board[nr][nc]:
                    return f'Robot {robot} crashes into robot {board[nr][nc]}'

                robot_pos[robot] = [nr, nc]
                board[r][c] = 0
                board[nr][nc] = robot

        else:
            if oper == 'R':
                robot_dir[robot] = ROTATE_R[(ROTATE_R.find(robot_dir[robot]) + iter) % 4]
            else:
                robot_dir[robot] = ROTATE_L[(ROTATE_L.find(robot_dir[robot]) + iter) % 4]
    return 'OK'

print(solution())
