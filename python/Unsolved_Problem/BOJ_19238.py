import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n_map, n_client, n_fuel = map(int ,input().split())

board = [list(map(int, input().split())) for _ in range(n_map)]
client_map = [[0] * n_map for _ in range(n_map)]
visit_client = [False] * (n_client+1)

start_r, start_c = map(int, input().split())

for i in range(1, n_client+1):
    cl_s_r, cl_s_c, cl_e_r, cl_e_c = map(int, input().split())
    client_map[cl_s_r-1][cl_s_c-1], client_map[cl_e_r-1][cl_e_c-1] = i, -i

# print(f'[debug]  client_map')
# for i in client_map:
#     print(*i)
# print('------------------------')

def get_client(start_r, start_c, rest_fuel):
    q = deque()
    q.append((start_r, start_c, rest_fuel))
    visited = set()
    visited.add((start_r, start_c))
    fuel_flag = 0
    client_list = []
    while q:
        x, y, p_fuel = q.popleft()
        # print(f'[debug]  x:{x}, y:{y}, p_fuel:{p_fuel}')
        if p_fuel < 0:
            return -1, -1, -1, -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_map and 0 <= ny < n_map):
                continue
            if (nx, ny) in visited:
                continue
            if board[nx][ny]: # wall
                continue
            if p_fuel < fuel_flag:
                continue
            if client_map[nx][ny] > 0 and not visit_client[client_map[nx][ny]]:
                fuel_flag = p_fuel
                client_list.append((nx, ny))
                visited.add((nx, ny))
            else:
                q.append((nx, ny, p_fuel - 1))
                visited.add((nx, ny))
    if not client_list:
        return -1, -1, -1, -1
    client_list.sort()
    # print(f'[debug]  client_list: {client_list}')
    next_client = client_map[client_list[0][0]][client_list[0][1]]
    visit_client[next_client] = True
    # print(f'[debug]  visit_client: {visit_client}')
    return client_list[0][0], client_list[0][1], fuel_flag-1, next_client

def client_to_dest(start_r, start_c, n_fuel, client):
    q = deque()
    q.append((start_r, start_c, n_fuel))
    visited = set()
    visited.add((start_r, start_c))
    while q:
        x, y, p_fuel = q.popleft()
        if p_fuel == 0:
            return -1, -1, -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n_map and 0 <= ny < n_map):
                continue
            if (nx, ny) in visited:
                continue
            if board[nx][ny]:  # wall
                continue
            if client_map[nx][ny] == -client:
                return nx, ny, p_fuel-1 + (n_fuel - p_fuel + 1)*2

            q.append((nx, ny, p_fuel-1))


def solution():
    sol_start_r, sol_start_c, sol_fuel = start_r, start_c, n_fuel
    for i in range(1, n_client+1):
        next_r, next_c, next_fuel, client = get_client(sol_start_r, sol_start_c, sol_fuel)
        # print(f'[debug]  get_client -> {(next_r, next_c, next_fuel, client)}')
        if next_r == -1:
            return -1
        sol_start_r, sol_start_c, sol_fuel = client_to_dest(next_r, next_c, next_fuel, client)
        if sol_start_c == -1:
            return -1
    return sol_fuel

print(solution())
