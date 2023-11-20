import sys

input = sys.stdin.readline

def solution():
    n_size = int(input())
    board = [[0] * n_size for _ in range(n_size)]
    for r in range(n_size):
        line = list(map(int, input().split()))
        for c, num in enumerate(line):
            board[r][c] = num
    
    # [up, left, down, right]
    F = ((-1, 0), (0, -1), (1, 0), (0, 1))
    L = ((0, -1), (1, 0), (0, 1), (-1, 0))
    R = ((0, 1), (-1, 0), (0, -1), (1, 0))
    # without 5%
    ratios = (1, 2, 7, 10)
    ratio_F = (-1, 0, 0, 1)
    ratio_LR = (1, 2, 1, 1)

    def spread(r, c, way):
        sand = board[r][c]
        remain = sand
        out = 0
        for i, ratio in enumerate(ratios):
            p = int(sand * 0.01 * ratio)
            if p > 0:
                for O in (L, R):
                    nr = r + F[way][0] * ratio_F[i] + O[way][0] * ratio_LR[i]
                    nc = c + F[way][1] * ratio_F[i] + O[way][1] * ratio_LR[i]
                    if 0 <= nr < n_size and 0 <= nc < n_size:
                        board[nr][nc] += p
                    else:
                        out += p
                remain -= 2 * p
        # 5%
        p5 = int(sand * 0.05)
        if p5 > 0:
            nr = r + F[way][0] * 2
            nc = c + F[way][1] * 2
            if 0 <= nr < n_size and 0 <= nc < n_size:
                board[nr][nc] += p5
            else:
                out += p5
            remain -= p5
        # remain
        nr = r + F[way][0] * 1
        nc = c + F[way][1] * 1
        if 0 <= nr < n_size and 0 <= nc < n_size:
            board[nr][nc] += remain
        else:
            out += remain
        # clear
        board[r][c] = 0

        return out
    
    def move(r, c, way):
        nr = r + F[way][0]
        nc = c + F[way][1]
        if nr + nc == n_size - 1:
            way = (way + 1) % 4
        elif nr <= (n_size // 2) and (nr == nc + 1):
            way = (way + 1) % 4
        elif nr > (n_size // 2) and (nr == nc):
            way = (way + 1) % 4
        return nr, nc, way

    result = 0
    
    r = c = n_size // 2
    way = 1
    cnt = 0
    while r >= 0 and c >= 0:
        nr, nc, nway = move(r, c, way)
        result += spread(nr, nc, way)
        cnt += 1
        r, c, way = nr, nc, nway
    print(result)

solution()