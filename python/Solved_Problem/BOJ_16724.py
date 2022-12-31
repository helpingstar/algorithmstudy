import sys

input = sys.stdin.readline

n_row, n_col = map(int, input().split())

parent = []

for i in range(n_row):
    line = []
    for j in range(n_col):
        line.append((i, j))
    parent.append(line)

def find(parent, pos):
    x, y = pos
    if parent[x][y] != (x, y):
        parent[x][y] = find(parent, parent[x][y])
    return parent[x][y]

def union(parent, pos_a, pos_b):
    pos_a = find(parent, pos_a)
    pos_b = find(parent, pos_b)

    ax, ay = pos_a
    bx, by = pos_b

    if pos_a < pos_b:
        parent[bx][by] = pos_a
    else:
        parent[ax][ay] = pos_b

def next_pos(x, y):
    if board[x][y] == 'D':
        return x+1, y
    elif board[x][y] == 'U':
        return x-1, y
    elif board[x][y] == 'L':
        return x, y-1
    else:
        return x, y+1

board = [list(input().rstrip()) for _ in range(n_row)]

for r in range(n_row):
    for c in range(n_col):
        union(parent, (r, c), next_pos(r, c))

check = set()

for r in range(n_row):
    for c in range(n_col):
        check.add(find(parent, (r, c)))

print(len(check))
