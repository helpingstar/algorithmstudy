import sys
from collections import deque
input = sys.stdin.readline

n_row, n_col = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n_row)]
for r in range(n_row):
    for c in range(n_col):
        if board[r][c] == 'R':
            r_x, r_y = r, c
            board[r][c] = '.'
        elif board[r][c] == 'B':
            b_x, b_y = r, c
            board[r][c] = '.'

visited = set()

def lefter_color(r_x, r_y, b_x, b_y):
    if r_y < b_y:
        return 'r'
    else:
        return 'b'

def higher_color(r_x, r_y, b_x, b_y):
    if r_x < b_x:
        return 'r'
    else:
        return 'b'

def spin_up(r_x, r_y, b_x, b_y):
    for next_r_x in range(r_x-1, -1, -1):
        if board[next_r_x][r_y] == '#':
            n_r_x = next_r_x + 1
            break
        elif board[next_r_x][r_y] == 'O':
            n_r_x, r_y = -1, -1
            break

    for next_b_x in range(b_x-1, -1, -1):
        if board[next_b_x][b_y] == '#':
            n_b_x = next_b_x + 1
            break
        elif board[next_b_x][b_y] == 'O':
            n_b_x, b_y = -1, -1
            break

    if (n_r_x, r_y) == (n_b_x, b_y) and (n_r_x, r_y) != (-1, -1):
        if higher_color(r_x, r_y, b_x, b_y) == 'r':
            n_b_x += 1
        else:
            n_r_x += 1

    return (n_r_x, r_y, n_b_x, b_y)

def spin_down(r_x, r_y, b_x, b_y):
    for next_r_x in range(r_x+1, n_row):
        if board[next_r_x][r_y] == '#':
            n_r_x = next_r_x - 1
            break
        elif board[next_r_x][r_y] == 'O':
            n_r_x, r_y = -1, -1
            break

    for next_b_x in range(b_x+1, n_row):
        if board[next_b_x][b_y] == '#':
            n_b_x = next_b_x - 1
            break
        elif board[next_b_x][b_y] == 'O':
            n_b_x, b_y = -1, -1
            break

    if (n_r_x, r_y) == (n_b_x, b_y) and (n_r_x, r_y) != (-1, -1):
        if higher_color(r_x, r_y, b_x, b_y) == 'r':
            n_r_x -= 1
        else:
            n_b_x -= 1

    return (n_r_x, r_y, n_b_x, b_y)

def spin_left(r_x, r_y, b_x, b_y):
    for next_r_y in range(r_y-1, -1, -1):
        if board[r_x][next_r_y] == '#':
            n_r_y = next_r_y + 1
            break
        elif board[r_x][next_r_y] == 'O':
            r_x, n_r_y = -1, -1
            break

    for next_b_y in range(b_y-1, -1, -1):
        if board[b_x][next_b_y] == '#':
            n_b_y = next_b_y + 1
            break
        elif board[b_x][next_b_y] == 'O':
            b_x, n_b_y = -1, -1
            break

    if (r_x, n_r_y) == (b_x, n_b_y) and (r_x, n_r_y) != (-1, -1):
        if lefter_color(r_x, r_y, b_x, b_y) == 'r':
            n_b_y += 1
        else:
            n_r_y += 1

    return (r_x, n_r_y, b_x, n_b_y)

def spin_right(r_x, r_y, b_x, b_y):
    for next_r_y in range(r_y+1, n_col):
        if board[r_x][next_r_y] == '#':
            n_r_y = next_r_y - 1
            break
        elif board[r_x][next_r_y] == 'O':
            r_x, n_r_y = -1, -1
            break

    for next_b_y in range(b_y+1, n_col):
        if board[b_x][next_b_y] == '#':
            n_b_y = next_b_y - 1
            break
        elif board[b_x][next_b_y] == 'O':
            b_x, n_b_y = -1, -1
            break

    if (r_x, n_r_y) == (b_x, n_b_y) and (r_x, n_r_y) != (-1, -1):
        if lefter_color(r_x, r_y, b_x, b_y) == 'r':
            n_r_y -= 1
        else:
            n_b_y -= 1

    return (r_x, n_r_y, b_x, n_b_y)

def bfs(r_x, r_y, b_x, b_y):
    q = deque()
    visited.add((r_x, r_y, b_x, b_y))
    q.append((r_x, r_y, b_x, b_y, 0))
    while q:
        r_x, r_y, b_x, b_y, cnt = q.popleft()
        # print(f'[debug]  {(r_x, r_y, b_x, b_y, cnt)}')
        if cnt == 10:
            return -1
        for func in [spin_up, spin_down, spin_left, spin_right]:
            n_r_x, n_r_y, n_b_x, n_b_y = func(r_x, r_y, b_x, b_y)
            if (n_r_x, n_r_y, n_b_x, n_b_y) in visited:
                continue
            if n_b_x == -1:
                continue
            if n_r_x == -1:
                return cnt+1
            q.append((n_r_x, n_r_y, n_b_x, n_b_y, cnt+1))
            visited.add((n_r_x, n_r_y, n_b_x, n_b_y))
            # print(f'[debug]: {(r_x, r_y, b_x, b_y)} -> {((n_r_x, n_r_y, n_b_x, n_b_y))}')
    return -1

print(bfs(r_x, r_y, b_x, b_y))
