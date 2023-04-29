import sys
import math

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

size = N // 2

for i in range(int(math.log2(N))):
    new_board = [[0] * size for _ in range(size)]

    for r in range(size):
        for c in range(size):
            new_board[r][c] = sorted(
                [board[2*r][2*c], board[2*r+1][2*c], board[2*r][2*c+1], board[2*r+1][2*c+1]])[2]

    # print('-'*20)
    # for l in new_board:
    #     print(l)
    # print('-'*20)

    size //= 2
    board = new_board

print(board[0][0])
