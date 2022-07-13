import sys

input = sys.stdin.readline

n, q = map(int, input().split())
n_line = 2 << n
board = []

for _ in range(n_line):
    board.append(list(map(int, input().split())))

querys = list(map(int, input().split()))

for query in querys:
    