import sys

input = sys.stdin.readline

def get_color(size, N, K, r, c):
    b_left = (N - K) // 2
    b_right = b_left + K - 1

    left = up = 0
    while size >= N:
        size //= N

        pos_r = (r - up) // size
        pos_c = (c - left) // size

        if (b_left <= pos_r <= b_right) and (b_left <= pos_c <= b_right):
            return 1

        left = left + pos_c * size
        up = up + pos_r * size

    return 0

def solution():
    s, N, K, R1, R2, C1, C2 = map(int, input().split())

    size = N ** s

    for r in range(R1, R2 + 1):
        for c in range(C1, C2 + 1):
            print(get_color(size, N, K, r, c), end='')
        print()

solution()
