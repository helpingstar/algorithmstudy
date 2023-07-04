import sys


def solve():
    input = sys.stdin.readline
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    ITER = min(R, C)

    spins = [T % (2*(R-2*i-1) + 2*(C-2*i-1)) for i in range(ITER // 2)]

    for i in range(ITER // 2):
        for _ in range(spins[i]):
            temp = board[i][i]
            board[i][i:C-1-i] = board[i][i+1:C-i]
            for j in range(R-2*i-1):
                board[i+j][C-1-i] = board[i+j+1][C-1-i]
            board[R-1-i][i+1:C-i] = board[R-1-i][i:C-1-i]
            for j in range(R-2*i-2):
                board[R-1-j-i][i] = board[R-j-2-i][i]
            board[i+1][i] = temp

    for line in board:
        print(*line)


if __name__ == "__main__":
    solve()
