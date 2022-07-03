import sys

input = sys.stdin.readline

turn_right = ['N', 'E', 'S', 'W']
turn_left = ['N', 'W', 'S', 'E']

way_to_num_left = {'N':0, 'W':1, 'S':2, 'E':3}
way_to_num_right = {'N':0, 'E':1, 'S':2, 'W':3}

num_to_way = []

def next_way(num, order, now):
    if order == 'L':
        return turn_left[(way_to_num_left[now] + num) % 4]
    else:
        return turn_right[(way_to_num_left[now] + num) % 4]

def next_pos(robot_info, num):
    x, y, way = robot[robot_info][0], robot[robot_info][1], robot[robot_info][2]
    if way == 'N':
        return x, y+num
    elif way == 'W':
        return x-num, y
    elif way == 'E':
        return x+num, y
    else:
        return x, y-num

def solution():

    for i in range(n):
        x, y, way = input().split()
        x, y = int(x), int(y)
        robot.append([x, y, way])
        board[x][y] = i+1

    for _ in range(m):
        n_robot, order, num = input().split()
        n_robot, num = int(n_robot), int(num)
        if order in ['L', 'R']:
            robot[n_robot][2] = next_way(num, order, robot[n_robot][2])
        else:
            n_x, n_y = next_pos(n_robot, num)
            r_x, r_y, r_way = robot[n_robot]
            
            if r_way == 'N':
                for i in range(r_y+1, min(r, n_y)+1):
                    if board[n_x][i] != 0:
                        return 'Robot {} crashes into robot {}'.format(n_robot, board[n_x][i])
                if not (0 < n_y <= r):
                    return 'Robot {} crashes into the wall'.format(n_robot)
                robot[n_robot][1] = n_y
            elif r_way == 'S':
                for i in range(r_y+1, max(0, n_y)-1, -1):
                    if board[n_x][i] != 0:
                        return 'Robot {} crashes into robot {}'.format(n_robot, board[i][n_y])
                if not (0 < n_y <= r):
                    return 'Robot {} crashes into the wall'.format(n_robot)
                robot[n_robot][1] = n_y
            elif r_way == 'E':
                for i in range(r_x+1, min(c, n_x)+1):
                    if board[i][n_y] != 0:
                        return 'Robot {} crashes into robot {}'.format(n_robot, board[i][n_y])
                if not (0 < n_x <= c):
                    return 'Robot {} crashes into the wall'.format(n_robot)
                robot[n_robot][0] = n_x
            else:
                for i in range(r_x+1, max(0, n_x)-1, -1):
                    if board[i][n_y] != 0:
                        return 'Robot {} crashes into robot {}'.format(n_robot, board[n_x][i])
                if not (0 < n_x <= c):
                    return 'Robot {} crashes into the wall'.format(n_robot)
                robot[n_robot][0] = n_x
    return 'OK'

c, r = map(int, input().split())
n, m = map(int, input().split())
board = [[0] * (r+1) for _ in range(c+1)]
robot = [[]]
print(solution())
