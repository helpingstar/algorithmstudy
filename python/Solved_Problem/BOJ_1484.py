import sys


def solution():
    input = sys.stdin.readline
    n = int(input())

    if n < 3:
        print(-1)
        return

    end = n // 2 + 1

    board = tuple(i * i for i in range(1, end + 1))
    l, r = 0, 1

    ans = []

    while l < r and r < end:
        temp = board[r] - board[l]
        if temp < n:
            r += 1
        elif temp > n:
            l += 1
        else:
            ans.append(r + 1)
            l += 1
            r += 1

    if ans:
        print(*ans, sep="\n")
    else:
        print(-1)


solution()
