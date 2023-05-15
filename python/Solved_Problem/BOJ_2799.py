import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = []

def checker(r, c):
    for i in range(4):
        if board[r+i][c] == '.':
            return i
    return 4

for _ in range(5*R + 1):
    board.append(input().rstrip())

result = [0] * 5

for r in range(R):
    for c in range(C):
        result[checker(1 + 5*r, 1 + 5*c)] += 1

print(*result)
