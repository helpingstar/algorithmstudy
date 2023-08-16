import sys

def solution():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    size = int(input())
    position = dict()
    wish = dict()
    board = [[0] * size for _ in range(size)]
    good_list = (0, 1, 10, 100, 1000)
    for _ in range(size * size):
        wish_number = [[0] * size for _ in range(size)]
        wish_max = 0
        line = list(map(int, input().split()))
        wish[line[0]] = line[1:]
        for w in range(1, 5):
            if line[w] in position:
                x, y = position[line[w]]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < size and 0 <= ny < size):
                        continue
                    if board[nx][ny] != 0:
                        continue
                    wish_number[nx][ny] += 1
                    wish_max = max(wish_max, wish_number[nx][ny])
        candidates = []
        for r in range(size):
            for c in range(size):
                if wish_number[r][c] == wish_max and board[r][c] == 0:
                    cnt = 0
                    for i in range(4):
                        nr = r + dx[i]
                        nc = c + dy[i]
                        if not (0 <= nr < size and 0 <= nc < size):
                            continue
                        if board[nr][nc] != 0:
                            continue
                        cnt += 1
                    candidates.append((-cnt, r, c))
        cnt, r, c = min(candidates)
        cnt *= -1
        board[r][c] = line[0]
        position[line[0]] = (r, c)
        # print(board)
    ans = 0
    for r in range(size):
        for c in range(size):
            num = board[r][c]
            cnt = 0
            # print(num)
            for n in wish[num]:
                x, y = position[n]
                if abs(r - x) + abs(c - y) == 1:
                    cnt += 1
            ans += good_list[cnt]
    print(ans)

solution()
