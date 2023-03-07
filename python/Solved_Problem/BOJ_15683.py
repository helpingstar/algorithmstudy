import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

cctv_list = []


def light(x, y, way):
    if way == 0:  # up
        dx, dy = -1, 0
    elif way == 1:  # down
        dx, dy = 1, 0
    elif way == 2:  # left
        dx, dy = 0, -1
    else:  # right
        dx, dy = 0, 1

    light_set = set()

    x += dx
    y += dy
    while (0 <= x < R and 0 <= y < C) and (board[x][y] != 6):
        light_set.add((x, y))
        x += dx
        y += dy

    return light_set


def cctv(x, y):
    temp_list = []
    if board[x][y] == 1:
        for i in range(4):
            temp_list.append(light(x, y, i))
    elif board[x][y] == 2:
        temp_list.append(light(x, y, 0) | light(x, y, 1))
        temp_list.append(light(x, y, 2) | light(x, y, 3))
    elif board[x][y] == 3:
        temp_list.append(light(x, y, 0) | light(x, y, 2))
        temp_list.append(light(x, y, 0) | light(x, y, 3))
        temp_list.append(light(x, y, 1) | light(x, y, 2))
        temp_list.append(light(x, y, 1) | light(x, y, 3))
    elif board[x][y] == 4:
        all = set()
        for i in range(4):
            all |= light(x, y, i)
        for i in range(4):
            temp_list.append(all - light(x, y, i))
    elif board[x][y] == 5:
        all = set()
        for i in range(4):
            all |= light(x, y, i)
        temp_list.append(all)
    else:
        return
    cctv_list.append(temp_list)
    return


base = set()
cnt = 0
for r in range(R):
    for c in range(C):
        if board[r][c] != 0:
            base.add((r, c))
            cctv(r, c)
answer = R * C

count_table = [0] * len(cctv_list)


def dfs(cnt):
    global answer
    if cnt == len(cctv_list):
        result = base.copy()
        for i in range(len(cctv_list)):
            result |= cctv_list[i][count_table[i]]
        answer = min(answer, R * C - len(result))
        return

    for i in range(len(cctv_list[cnt])):
        count_table[cnt] = i
        dfs(cnt+1)


dfs(0)

print(answer)
