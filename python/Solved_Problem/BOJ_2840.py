import sys

input = sys.stdin.readline

def solution():
    n_cell, T = map(int, input().split())
    board = ['?'] * n_cell
    cur = 0
    check = set()
    for _ in range(T):
        a, b = input().split()
        a = int(a)

        n_cur = (cur - a) % n_cell

        if board[n_cur] != '?' and board[n_cur] != b:
            return "!"
        else:
            if b in check and board[n_cur] == "?":
                return "!"
            board[n_cur] = b
            check.add(b)

        cur = n_cur
    return ''.join(board[cur:]) + ''.join(board[:cur])

print(solution())
