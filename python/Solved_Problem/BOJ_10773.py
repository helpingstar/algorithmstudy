import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    num = int(input())

    if num == 0:
        board.pop()
    else:
        board.append(num)

print(sum(board))
