import sys

input = sys.stdin.readline

n_board, n_client, fuel = map(int, input().split())

board = []

for _ in range(n_board):
    board.append(list(map(int, input().split())))

start_x, start_y = map(int, input().split())

clients = []

for _ in range(n_client):
    clients.append(list(map(int, input().split())))

