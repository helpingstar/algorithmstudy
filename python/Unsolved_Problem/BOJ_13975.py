import sys

input = sys.stdin.readline

# INF = 10000000000


def solution():
    N = int(input())

    nums = list(map(int, input().split()))
    sums = [0] * (N+1)
    for i in range(N):
        sums[i+1] = sums[i] + nums[i]

    board = [[0] * N for _ in range(N)]

    for size in range(1, N+1):          # 1, 2, 3, 4
        for start in range(0, N-size):  # 3, 2, 1, 0
            end = start + size
            print(start, end, size)
            temp = float('inf')
            for i in range(start, end):
                temp = min(temp, board[start][i]+board[i+1][end])
            board[start][end] = temp + sums[end+1] - sums[start]

    # for i in board:
    #     print(i)
    return board[0][-1]


for _ in range(int(input())):
    print(solution())
