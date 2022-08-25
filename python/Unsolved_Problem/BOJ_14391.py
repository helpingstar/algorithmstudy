import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().rstrip())))

x1, y1, x2, y2 = 0, 0, n, m

done = False

while not done:
    if x2 - x1 > y2 - y1:
        