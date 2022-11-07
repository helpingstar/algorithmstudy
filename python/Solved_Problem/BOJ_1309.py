n = int(input())

board = [[1, 1, 1], [1, 1, 1]]

for _ in range(n-1):
    board[0] = board[1][:]
    board[1][0] = sum(board[0]) % 9901
    board[1][1] = board[1][2] = board[1][0] - board[0][1]

print(sum(board[1]) % 9901)
