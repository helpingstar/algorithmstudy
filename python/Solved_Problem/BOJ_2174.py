import sys

input = sys.stdin.readline

def solution():
    C, R = map(int, input().split())
    N, M = map(int, input().split())

    board = [[0] * C for _ in range(R)]
    robots = [[-1, -1, 'O'] for _ in range(N + 1)]
    NEWS = ["N", "W", "S", "E"]
    NEWS_index = {"N": 0, "W": 1, "S": 2, "E": 3}
    delta = {"N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)}

    for i in range(N):
        x, y, way = input().split()
        x = int(x) - 1
        y = R - int(y)
        robots[i + 1] = [y, x, way]
        board[y][x] = i + 1

    orders = []
    for _ in range(M):
        robot, order, repeat = input().split()
        orders.append((int(robot), order, int(repeat)))

    for robot, order, repeat in orders:
        if order == "L":
            way = robots[robot][2]
            robots[robot][2] = NEWS[(NEWS_index[way] + repeat) % 4]
        elif order == "R":
            way = robots[robot][2]
            robots[robot][2] = NEWS[(NEWS_index[way] - repeat) % 4]
        else:
            robot_r, robot_c, way = robots[robot]
            board[robot_r][robot_c] = 0
            dr, dc = delta[way]
            for _ in range(repeat):
                robot_r += dr
                robot_c += dc
                if not (0 <= robot_r < R and 0 <= robot_c < C):
                    return f"Robot {robot} crashes into the wall"
                if board[robot_r][robot_c] != 0:
                    return f"Robot {robot} crashes into robot {board[robot_r][robot_c]}"
            robots[robot] = [robot_r, robot_c, way]

    return "OK"

print(solution())
