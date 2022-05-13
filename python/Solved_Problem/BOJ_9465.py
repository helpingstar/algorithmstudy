import sys

input = sys.stdin.readline

t = int(input())

def solution():
    n = int(input())

    board = []

    board.append(list(map(int, input().split())))
    board.append(list(map(int, input().split())))

    if n == 1:
        return max(board[0][0], board[1][0])
    elif n == 2:
        return max(board[0][0] + board[1][1], board[0][1] + board[1][0])
    else:
        board[0][1] += board[1][0]
        board[1][1] += board[0][0]
        for i in range(2, n):
            board[0][i] += max(board[1][i-2], board[1][i-1])
            board[1][i] += max(board[0][i-2], board[0][i-1])
    
    return max(board[0][n-1], board[1][n-1])

for _ in range(t):
    print(solution())