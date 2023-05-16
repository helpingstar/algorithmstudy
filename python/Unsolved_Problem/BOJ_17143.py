import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[[] for _ in range()]]
# s : 속력
# d : 방향
#   1 : 위
#   2 : 아래
#   3 : 오른쪽
#   4 : 왼쪽
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c]