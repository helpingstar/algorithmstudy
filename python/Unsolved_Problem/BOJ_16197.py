import sys

input = sys.stdin.readline

x, y = map(int, input().split())

board = [input().rstrip() for _ in range(x)]

coins = []

for i in range(x):
    for j in range(y):
        if board[x][y] == 'o':
            coins.append([x, y])

