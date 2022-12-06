import sys
from collections import deque
input = sys.stdin.readline

# (x, y, 상태)
# 상태 0: ---, 1: |

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]

start_pos = []
target_pos = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            start_pos.append((i, j))
        elif board[i][j] == 'E':
            target_pos.append((i, j))

sx, sy = start_pos[1]
if start_pos[0][0] == start_pos[1][0]:
    s_state = 0
else:
    s_state = 1
tx, ty = target_pos[1]
if target_pos[0][0] == target_pos[1][0]:
    t_state = 0
else:
    t_state = 1

def check_u(r, c, state):
    if state == 0:  # ---
        if r == 0:
            return False
        for i in range(-1, 2):
            if board[r-1][c+i] == '1':
                return False
    else:  # |
        if r <= 1:
            return False
        if board[r-2][c] == '1':
            return False
    return True

def check_d(r, c, state):
    if state == 0: # ---
        if r == N-1:
            return False
        for i in range(-1, 2):
            if board[r+1][c+i] == '1':
                return False
    else:  # |
        if r >= N-2:
            return False
        if board[r+2][c] == '1':
            return False
    return True

def check_l(r, c, state):
    if state == 0: # ---
        if c <= 1:
            return False
        if board[r][c-2] == '1':
            return False
    else:  # |
        if c == 0:
            return False
        for i in range(-1, 2):
            if board[r+i][c-1] == '1':
                return False
    return True

def check_r(r, c, state):
    if state == 0:  # ---
        if c >= N-2:
            return False
        if board[r][c+2] == '1':
            return False
    else:  # |
        if c == N-1:
            return False
        for i in range(-1, 2):
            if board[r+i][c+1] == '1':
                return False
    return True

def check_turn(r, c, state):
    if not (1 <= r < N-1 and 1 <= c < N-1):
        return False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if board[r+i][c+j] == '1':
                return False
    return True

def check_possible_action(r, c, state):
    action_list = []
    if check_u(r, c, state):
        action_list.append('u')
    if check_d(r, c, state):
        action_list.append('d')
    if check_l(r, c, state):
        action_list.append('l')
    if check_r(r, c, state):
        action_list.append('r')
    if check_turn(r, c, state):
        action_list.append('t')
    return action_list

def next_pos(r, c, state, action_list):
    next_pos_list = []
    for action in action_list:
        if action == 'u':
            next_pos_list.append((r-1, c, state))
        elif action == 'd':
            next_pos_list.append((r+1, c, state))
        elif action == 'l':
            next_pos_list.append((r, c-1, state))
        elif action == 'r':
            next_pos_list.append((r, c+1, state))
        elif action == 't':
            next_state = 0 if state == 1 else 1
            next_pos_list.append((r, c, next_state))
    return next_pos_list

def bfs(sx, sy, s_state):
    q = deque()
    q.append((sx, sy, s_state, 0))
    visited = set()
    visited.add((sx, sy, s_state))
    while q:
        x, y, state, count = q.popleft()
        # print(f'[debug]  ({x}, {y}), {state}')
        possible_action = check_possible_action(x, y, state)
        next_pos_list = next_pos(x, y, state, possible_action)
        for nx, ny, n_state in next_pos_list:
            if (nx, ny, n_state) in visited:
                continue
            if (nx, ny, n_state) == (tx, ty, t_state):
                return count+1
            q.append((nx, ny, n_state, count+1))
            visited.add((nx, ny, n_state))
    return 0

print(bfs(sx, sy, s_state))
