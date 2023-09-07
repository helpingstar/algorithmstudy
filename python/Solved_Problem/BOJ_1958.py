import sys

input = sys.stdin.readline


def solution():
    wordi = list(input().rstrip())
    wordj = list(input().rstrip())
    wordk = list(input().rstrip())

    board = [[[0] * (len(wordi)+1) for _ in range(len(wordj)+1)]
             for _ in range(len(wordk)+1)]
    # print(board)
    for k in range(len(wordk)):
        for j in range(len(wordj)):
            for i in range(len(wordi)):
                if (wordi[i] == wordj[j]) and (wordj[j] == wordk[k]):
                    board[k+1][j+1][i+1] = board[k][j][i] + 1
                else:
                    board[k+1][j+1][i+1] = max(board[k][j+1][i+1],
                                               board[k+1][j][i+1], board[k+1][j+1][i])
    print(board[-1][-1][-1])


solution()
