import sys

MOD = 1000000009

input = sys.stdin.readline

T = int(input())

nums = [int(input()) for _ in range(T)]

end = max(max(nums), 4)

board = [[0, 0, 0] for _ in range(end+1)]

board[1][0] = 1
board[2][1] = 1
board[3][0], board[3][1], board[3][2] = 1, 1, 1

for i in range(4, end+1):
    board[i][0] = (board[i-1][1] + board[i-1][2]) % MOD
    board[i][1] = (board[i-2][0] + board[i-2][2]) % MOD
    board[i][2] = (board[i-3][0] + board[i-3][1]) % MOD

for num in nums:
    print(sum(board[num]) % MOD)
