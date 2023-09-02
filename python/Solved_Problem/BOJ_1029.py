import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(N)]
    people = [[[0 for _ in range(10)] for _ in range(1 << N)] for _ in range(N)]

    def dp(now, visited, price):
        if people[now][visited][price] != 0:
            return people[now][visited][price]

        n_max = 0
        for i in range(1, N):
            if visited & (1 << i) != 0:
                continue
            if price > board[now][i]:
                continue
            n_max = max(n_max, 1 + dp(i, visited | (1 << i), board[now][i]))
        people[now][visited][price] = n_max
        return n_max

    print(1 + dp(0, 1, 0))
    return


solution()
