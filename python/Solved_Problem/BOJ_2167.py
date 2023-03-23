import sys

input = sys.stdin.readline

R, C = map(int, input().split())

sum_board = [[0] * (C+1) for _ in range(R+1)]

for r in range(R):
    temp = [0] * (C+1)
    nums = list(map(int, input().split()))

    for c in range(C):
        temp[c+1] = temp[c] + nums[c]

    for c in range(C+1):
        sum_board[r+1][c] = sum_board[r][c] + temp[c]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_board[x2][y2] - sum_board[x2][y1-1] -
          sum_board[x1-1][y2] + sum_board[x1-1][y1-1])
