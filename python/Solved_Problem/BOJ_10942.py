import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

board = [[0] * n for _ in range(n)]

for length in range(n):
    for start in range(n-length):
        end = start + length

        if length == 0:
            board[start][end] = 1
            continue

        if nums[start] == nums[end]:
            if length == 1:
                board[start][end] = 1
            else:
                if board[start+1][end-1] == 1:
                    board[start][end] = 1

n_question = int(input())
for _ in range(n_question):
    a, b = map(int, input().split())
    print(board[a-1][b-1])
