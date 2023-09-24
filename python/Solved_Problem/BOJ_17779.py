import sys


def solution():
    input = sys.stdin.readline

    n_size = int(input())
    board = [list(map(int, input().split())) for _ in range(n_size)]
    ans = float("inf")
    total = 0
    for line in board:
        total += sum(line)

    for d1 in range(1, n_size - 1):
        for d2 in range(1, n_size - d1):
            up = (0, d1)
            left = (d1, 0)
            right = (d2, d1 + d2)
            down = (d1 + d2, d2)
            for dc in range(n_size - d1 - d2):
                for dr in range(n_size - d1 - d2):
                    n_up = (up[0] + dr, up[1] + dc)
                    n_left = (left[0] + dr, left[1] + dc)
                    n_right = (right[0] + dr, right[1] + dc)
                    n_down = (down[0] + dr, down[1] + dc)

                    populations = [0, 0, 0, 0, 0]
                    # 1, 2
                    for r in range(n_up[0]):
                        populations[0] += sum(board[r][: n_up[1] + 1])
                        populations[1] += sum(board[r][n_up[1] + 1 :])
                    # 1
                    cnt = 0
                    for r in range(n_up[0], n_left[0]):
                        populations[0] += sum(board[r][: n_up[1] - cnt])
                        cnt += 1
                    # 2
                    cnt = 1
                    for r in range(n_up[0], n_right[0] + 1):
                        populations[1] += sum(board[r][n_up[1] + cnt :])
                        cnt += 1
                    # 3, 4
                    for r in range(n_down[0] + 1, n_size):
                        populations[2] += sum(board[r][: n_down[1]])
                        populations[3] += sum(board[r][n_down[1] :])
                    # 3
                    cnt = 0
                    for r in range(n_left[0], n_down[0] + 1):
                        populations[2] += sum(board[r][: n_left[1] + cnt])
                        cnt += 1
                    # 4
                    cnt = 0
                    for r in range(n_right[0] + 1, n_down[0] + 1):
                        populations[3] += sum(board[r][n_right[1] - cnt :])
                        cnt += 1
                    populations[4] = total - sum(populations[:4])
                    # print(n_up, n_left, n_right, n_down)
                    # print(populations)
                    ans = min(ans, max(populations) - min(populations))
    print(ans)


solution()
