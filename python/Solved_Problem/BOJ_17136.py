import sys


def solution():
    input = sys.stdin.readline

    board = [list(map(int, input().split())) for _ in range(10)]
    papers = [0, 5, 5, 5, 5, 5]
    result = 25

    def check(r, c, size):
        for i in range(size):
            for j in range(size):
                if board[r + i][c + j] == 0:
                    return False
        return True

    def dp(r, c, p):
        # print(r, c, papers)
        nonlocal result
        if r == 10:
            result = min(result, p)
            return
        if c == 10:
            dp(r + 1, 0, p)
            return
        if board[r][c] == 1:
            for s in range(1, 6):
                if papers[s] == 0:
                    continue
                if c + s > 10 or r + s > 10:
                    break
                if not check(r, c, s):
                    break
                for i in range(s):
                    for j in range(s):
                        board[r + i][c + j] = 0
                papers[s] -= 1
                dp(r, c + s, p + 1)
                for i in range(s):
                    for j in range(s):
                        board[r + i][c + j] = 1
                papers[s] += 1
        else:
            dp(r, c + 1, p)

    dp(0, 0, 0)
    print(result if result != 25 else -1)


solution()
