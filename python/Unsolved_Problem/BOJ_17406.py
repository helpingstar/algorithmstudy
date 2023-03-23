import copy
import sys
from itertools import permutations

input = sys.stdin.readline

R, C, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(R)]

spins = [list(map(int, input().split())) for _ in range(K)]


def next_pos(r, c, k, x, y):
    if x == r - k and y < c + k:
        return x, y+1
    elif x == r + k and c - k < y:
        return x, y-1
    elif r - k < x and y == c - k:
        return x - 1, y
    else:
        return x + 1, y


def spinning(board, r, c, k):
    r -= 1
    c -= 1
    for i in range(1, k+1):
        x, y = r-k, c-k
        temp = board[x][y]
        temp2 = -1
        for _ in range(i*2*4):
            nx, ny = next_pos(r, c, k, x, y)
            print(board[0])
            temp2 = board[nx][ny]
            board[nx][ny] = temp

            temp = temp2
            x, y = nx, ny


spinning(board, *spins[0])

for i in board:
    print(i)
