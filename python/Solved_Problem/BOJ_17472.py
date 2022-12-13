import sys
from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

input = sys.stdin.readline

nRow, nCol = map(int, input().split())

board = []
assign_board = []
assign_visited = set()
for _ in range(nRow):
    line = list(map(int, input().split()))
    board.append(line)
    assign_board.append([0] * nCol)

def assign_island(x, y, name):
    q = deque()
    q.append((x, y))
    assign_visited.add((x, y))
    assign_board[x][y] = name
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < nRow and 0 <= ny < nCol):
                continue
            if (nx, ny) in assign_visited:
                continue
            if board[nx][ny] == 0:
                continue
            assign_visited.add((nx, ny))
            q.append((nx, ny))
            assign_board[nx][ny] = name
name = 1
for r in range(nRow):
    for c in range(nCol):
        if board[r][c] == 1 and (r, c) not in assign_visited:
            assign_island(r, c, name)
            name += 1
INF = 100000
graph = []
for _ in range(name):
    graph.append([INF] * name)

edges = []

for r in range(nRow):
    prev_name = assign_board[r][0]
    prev_pos = 0
    for c in range(1, nCol):
        if assign_board[r][c] != 0:
            now_name = assign_board[r][c]
            if assign_board[r][c] != prev_name:
                if c - prev_pos - 1 >= 2 and prev_name != 0:
                    # print(f'[debug]  {prev_name}-{now_name} : {c-prev_pos}')
                    # graph[prev_name][now_name] = min(c - prev_pos - 1, graph[prev_name][now_name])
                    # graph[now_name][prev_name] = graph[prev_name][now_name]
                    edges.append((c-prev_pos-1, prev_name, now_name))
                prev_name = now_name
            prev_pos = c

for c in range(nCol):
    prev_name = assign_board[0][c]
    prev_pos = 0
    for r in range(1, nRow):
        # print(f'[debug]  (r, c) : {(r, c)}, prev_pos:{prev_pos}, prev_name:{prev_name}')
        if assign_board[r][c] != 0:
            now_name = assign_board[r][c]
            if assign_board[r][c] != prev_name:
                if r - prev_pos - 1 >= 2 and prev_name != 0:
                    # print(f'[debug]  {prev_name}-{now_name} : {r-prev_pos-1}')
                    # graph[prev_name][now_name] = min(r - prev_pos - 1, graph[prev_name][now_name])
                    # graph[now_name][prev_name] = graph[prev_name][now_name]
                    edges.append((r - prev_pos - 1, prev_name, now_name))
                prev_name = now_name
            prev_pos = r


# print(*assign_board, sep='\n')
edges.sort()
# print(edges)
parent = [i for i in range(name)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a
result = 0
result_count = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        result_count += 1

if result_count == name-2:
    print(result)
else:
    print(-1)
